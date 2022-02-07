from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path("", views.PostList.as_view()),
    path("<int:pk>", views.PostDetail.as_view()),
    
]