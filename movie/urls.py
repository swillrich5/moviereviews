from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),

]