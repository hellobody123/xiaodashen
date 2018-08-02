from django.urls import path
from . import views
urlpatterns =[
    path('', views.index, name='index'),
    path('z/', views.sign_up, name='sign_up'),
    path('cz/', views.register, name='register'),
    path('d/', views.sign_in, name='sign_in'),
    path('cd/', views.log_in, name='log_in'),
    path('write/', views.write, name='write'),
    path('tc/', views.do_logout, name='do_logout')



]