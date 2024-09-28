from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('tuiton', views.TuitionViewSet)
router.register('subject', views.SubjectViewSet)
router.register('review', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('tuitions/review/<int:pk>/', views.ReviewViewSet.as_view(), name='review'),
    # path('tuitions/tuiton/<int:pk>/', views.TuitionViewSet.as_view(), name='tuition-detail'),
]