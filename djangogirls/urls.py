from django.urls import path
from . import views

app_name = 'djangogirls'

urlpatterns = [
    path('', views.index, name = 'basepage' ),
    path('community/', views.community, name= 'community'),
    path('resources/', views.resources, name= 'resources'),
  
]
