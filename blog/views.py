from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Kropka przed modelami models oznacza bieżący katalog lub bieżącą aplikację. views.py i models.py znajdują się w tym samym katalogu. Oznacza to, że możemy użyć . i nazwy pliku (bez .py). Następnie importujemy nazwę modelu (Post).

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
