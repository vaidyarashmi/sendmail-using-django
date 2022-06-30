from django.urls import path,include
from email_app import views
urlpatterns = [
    path('', views.home, name="home"),
]
