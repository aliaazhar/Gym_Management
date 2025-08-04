from  django.urls import path
from . import views


urlpatterns =[
    path('', views.main, name='main'),
    path('register/', views.register_member, name='register_member'),

]
