from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .models import Movie, Review
from .forms import ReviewForm

# Create your views here.
def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', 
                {'searchTerm': searchTerm, 'movies': movies})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})

def about(request):
    return HttpResponse('<h1>Welcome to Movie Reviews About Page</h1>')


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})


def createreview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        return render(request, 'createreview.html',
                        {
                            'form': ReviewForm(),
                            'movie': movie
                        })
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('movie:movie_detail', newReview.movie.id)
        except ValueError:
            return render(request, 'createreview.html', 
                            {
                                'form': ReviewForm(),
                                'error': 'bad data passed in'
                            })
