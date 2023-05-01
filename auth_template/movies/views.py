from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Genre, Movie
from rest_framework.decorators import api_view

from django.core.paginator import Paginator     # django 내장 페이징 기능


# Create your views here.
@require_safe
@api_view(['GET'])
def index(request):
    # movies = Movie.objects.all()
    # context = {
    #     'movies': movies,
    # }
    # return render(request, 'movies/index.html', context)
    movie_list = Movie.objects.all()
    # 15개씩 객체를 만든다
    paginator = Paginator(movie_list, 15)
    # page 매개변수를 가져와서 해당 페이지의 영화를 가져오도록 한다.
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    genre = movie.genres.all()
    context = {
        'movie': movie,
        'genres': genre,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    movies = Movie.objects.all().order_by('-vote_average', '-popularity')[:10]
    context = {
        'movies': movies,
    }
    return render(request, 'movies/recommended.html', context)
