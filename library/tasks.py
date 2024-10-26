from celery import shared_task
from django.utils import timezone
from .models import Book


@shared_task
def archive_book():
    threshold_date = timezone.now() - timezone.timedelta(days=365*10)
    books = Book.objects.filter(published_date__lte=threshold_date, is_archived=False)

    for book in books:
        book.is_archived = True
        book.save()
