from django.urls import path
from .views import UserRetrieveAPIView, UserUpdateAPIView, LoginAPIView

app_name = 'accounts'

urlpatterns = [
     path('login' ,LoginAPIView.as_view(), name='login'),
     path('retrieve/<int:pk>',UserRetrieveAPIView.as_view(), name='retrieve'),
     path('update/<int:pk>', UserUpdateAPIView.as_view(), name='update'),
]
