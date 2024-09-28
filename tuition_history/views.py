from django.shortcuts import render
from .serializers import Tuition_History_Serializer
from .models import UserTuitionHistory
from rest_framework import viewsets
from rest_framework.filters import BaseFilterBackend
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class Tuition_History_Filter_Using_ID(BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        user_id = request.query_params.get("user_id")
        if user_id:
            return query_set.filter(user_id = user_id)
        return query_set

class Tuition_History_Filter_Tuition_ID(BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        tuition_id = request.query_params.get("tuition_id")
        if tuition_id:
            return query_set.filter(tuition_id = tuition_id)
        return query_set

class Tuition_History_Viewset(viewsets.ModelViewSet):
    queryset = UserTuitionHistory.objects.all()
    serializer_class = Tuition_History_Serializer
    filter_backends = [Tuition_History_Filter_Using_ID, Tuition_History_Filter_Tuition_ID]
        
    # def patch(self, request, id, format=None):
    #     tuition_history = UserTuitionHistory.objects.get(id=id)
    #     serializer = Tuition_History_Serializer(tuition_history, data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
        
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)