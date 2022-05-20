from django.urls import path

from app.views import index_view

urlpatterns = [
    path('', index_view),
]
