from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterViews.as_view(), name='user_register'),
    path('verify/', views.UserRegistrVerifyCodeView.as_view(), name='verify_code'),
]

