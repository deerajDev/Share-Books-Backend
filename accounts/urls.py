from django.urls import path
from .views import RegisterAPIView, LoginAPIView ,  UserRetrieveAPIView, UserUpdateAPIView

app_name = 'accounts'

urlpatterns = [
     path('register' ,RegisterAPIView.as_view(), name='register'),
     path('login' ,LoginAPIView.as_view(), name='login'),
     path('retrieve',UserRetrieveAPIView.as_view(), name='retrieve'),
     path('update', UserUpdateAPIView.as_view(), name='update'),
]
