from django.urls import path
from .views import UserListAPIView

app_name = 'usersapp'
urlpatterns = [
    path('', UserListAPIView.as_view()),
]
