from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('list', views.UserViewset)
router.register('register_user_list', views.RegisteredUserViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationApiView.as_view(), name="register"),
    path('login/', views.UserLoginApiView.as_view(), name="login"),
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
    path('active/<uid64>/<token>/', views.activate, name="activate"),
    path('change_password/', views.ChangePassword.as_view(), name="change_password")
    # path('tuition_history/', views.UserTuitionHistoryView.as_view(), name='user-tuition-history'),
]
