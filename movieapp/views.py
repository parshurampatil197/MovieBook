from django.shortcuts import render
from movieapp.models import Movie
from movieapp.forms import MovieForm

def index_view(request):
    return render(request,'movieapp/index.html')

def list_movies_view(request):
    movies_list = Movie.objects.all()
    return render(request,'movieapp/listmovies.html',{'movies_list':movies_list})

def add_movie_view(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request,'movieapp/addmovie.html',{'form':form})
