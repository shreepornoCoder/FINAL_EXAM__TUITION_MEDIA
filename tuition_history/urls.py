from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('list', views.Tuition_History_Viewset)

urlpatterns = [
    path('', include(router.urls)),
]
