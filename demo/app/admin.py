from django.contrib import admin

from .forms import ArticleForm
from .models import Article


@admin.register(Article)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    form = ArticleForm
