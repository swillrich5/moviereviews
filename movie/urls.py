from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:movie_id>', views.movie_detail, name='movie_detail'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('movie/<int:movie_id>/create/', views.createreview, name="createreview"),
    path('movie/review/<int:review_id>', views.updatereview, name="updatereview"),
    path('movie/review/<int:review_id>/delete/', views.deletereview, name='deletereview'),
]