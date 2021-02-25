from django.urls import path

from . import views

urlpatterns = [
path('', views.homeViewPage, name='home')

]