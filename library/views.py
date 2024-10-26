from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@csrf_exempt
def filter_books(request):
    if request.method == 'POST':
        author_name = request.GET.get('author')
        genre = request.GET.get('genre')
        publish_start = request.GET.get('publish_start')
        publish_end = request.GET.get('publish_end')

        filters = {}

        if author_name:
            filters['author__name'] = author_name
        if genre:
            filters['genre'] = genre
        if publish_start:
            filters['publish_start__gte'] = parse_date(publish_start)
        if publish_end:
            filters['publish_end__lte'] = parse_date(publish_end)

        books = get_list_or_404(Book.objects.filter(**filters))

        books_list = [
            {
                'title' : book.title,
                'author' : book.author.name,
                'genre' : book.genre,
                'published_date': book.published_date,
            }
            for book in books
        ]

        return JsonResponse(books_list, safe=False)
    return JsonResponse({'error' : "Invalid Request ! "}, status=400)