from django.urls import path
from myapp import views

urlpatterns = [
    path("home/<int:number>", views.hello, name='home'),
    path('', views.index, name='index')
]