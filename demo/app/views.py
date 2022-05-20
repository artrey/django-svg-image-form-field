from django.shortcuts import render

from app.models import Article


def index_view(request):
    return render(request, 'app/index.html', {'object_list': Article.objects.all()})
