from django.shortcuts import render
from . import models
from .serializers import SubjectSerializers, ReviewSerializer, TuitionSerializer
from rest_framework import viewsets
from rest_framework.filters import BaseFilterBackend
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

# Create your views here.
class GradeFilterBackend(BaseFilterBackend):
    # serializer_class = serializers.TuitionSerializer
    def filter_queryset(self, request, query_set, view):
        grade = request.query_params.get("grade")
        if grade:
            return query_set.filter(grade = grade)
        return query_set

class TuitionViewSet(viewsets.ModelViewSet):
    queryset = models.Tuitions.objects.all()
    serializer_class = TuitionSerializer
    filter_backends = [GradeFilterBackend]

    # def get_object(self, pk):
    #     try:
    #         return models.Tuitions.objects.get(pk=pk)
    #     except models.Tuitions.DoesNotExist:
    #         return Http404

    # def get(self, request, pk, format=None):
    #     post = self.get_object(pk)
    #     serializer = TuitionSerializer(post)
    #     return Response(serializer.data)

    def put(self, request, pk, format=None):
        print("Inside put")
        post = self.get_object(pk)
        serializer = TuitionSerializer(post, request.data)
        if serializer.is_valid():
            print("serializer", serializer.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = models.Subjects.objects.all()
    serializer_class = SubjectSerializers

# Review Viewset 
class TuitionIDFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        tuition_id = request.query_params.get("tuition_id")

        if tuition_id:
            return query_set.filter(tuition_id=tuition_id)

        return query_set
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Reviews.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [TuitionIDFilterBackend]

