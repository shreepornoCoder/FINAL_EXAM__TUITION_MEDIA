from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from tuitions.models import Tuitions

GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
]

class UserSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    select_user = serializers.PrimaryKeyRelatedField(
        queryset=models.UserModel.objects.all(), source='users', many=True, write_only=True
    )
    class Meta:
        model = models.UserModel
        fields = "__all__"

class RegisterUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "username", "first_name", "last_name", "email", "password"]

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    educational_institute = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=300)
    gender = serializers.ChoiceField(choices=GENDER) 
    class Meta:
        model = models.User
        fields = ["username", "first_name", "last_name", "email", "password", "confirm_password", "educational_institute", "location", "gender"]
        
    def save(self):
        validated_data = self.validated_data
        account = User(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"]
        )
        account.set_password(validated_data["password"])
        account.is_active = False
        account.save()

        teacher_account = models.UserModel(
            user=account,
            educational_institute=validated_data["educational_institute"],
            location=validated_data["location"],
            gender=validated_data["gender"]
        )
        teacher_account.save()

        return account
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True)

class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required = True)
    new_password = serializers.CharField(required = True)

# class UserTuitionHistorySerializer(serializers.Serializer):
#     user = serializers.PrimaryKeyRelatedField(
#         queryset=models.UserModel.objects.all(), source='users', many=True, write_only=True
#     )
#     tuition = serializers.PrimaryKeyRelatedField(
#         queryset=Tuitions.objects.all(), source='tuition', many=True, write_only=True
#     )

#     class Meta:
#         model = models.UserTuitionHistory
#         fields = "__all__"