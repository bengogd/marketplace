from django.urls import path
from main import views


urlpatterns = [
    path('', views.home, name="home"),
    path('post/<int:pk>', views.service_detail, name='serv_detail'),
]
