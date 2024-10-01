from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import viewsets
from . import models 
from . import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

#sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    queryset = models.UserModel.objects.all()
    serializer_class = serializers.UserSerializers

class RegisteredUserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.RegisterUserSerializers

class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            print("inside is_valid()")
            user = serializer.save()
            token = default_token_generator.make_token(user)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"https://final-exam-tuition-media-64an.vercel.app/users/active/{uid}/{token}/"

            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link':confirm_link})

            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()

            return Response("Check Your Mail for Confirmation!")
        return Response(serializer.errors)

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)

    except(User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("register")
    
    else:
        return redirect("register")
    
class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data = self.request.data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            email = serializer.validated_data["email"]

            user = authenticate(username = username, password = password)

            if user:
                token, _ = Token.objects.get_or_create(user = user)
                login(request, user)
                print(user, user.id, user.profile.id) 
                return Response({"token":token.key, "user_id":user.id, "user_model_id": user.profile.id})
            else:
                return Response({"error":"Invalid Credential!"})
            
        return Response(serializer.errors)

class UserLogoutView(APIView):

    def get(self, request):
        print(request.user)
        # request.user.auth.delete()
        request.user.auth_token.delete()
        logout(request)
        
        return Response({"ok":"True"})
    
class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]  

    def put(self, request):
        
        user_id = request.data.get('user_id')
        old_password = request.data.get('password')
        new_password = request.data.get('new_password')

        print(user_id, old_password, new_password)
        
        if not user_id or not old_password or not new_password:
            return Response({
                'error': 'user_id, old_password, and new_password are required.'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            
            user = User.objects.get(id=user_id)

        except User.DoesNotExist:
            return Response({
                'error': 'User not found.'
            }, status=status.HTTP_404_NOT_FOUND)

        
        if not user.check_password(old_password):
            return Response({
                'error': 'Old password is incorrect.'
            }, status=status.HTTP_400_BAD_REQUEST)

        
        user.set_password(new_password)
        user.save()

        return Response({
            'message': 'Password changed successfully'
        }, status=status.HTTP_200_OK)

#12345ssts@
#01747264587