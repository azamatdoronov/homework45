from django.urls import path

from webapp.views import index_view

urlpatterns = [
    path('', index_view),
    path('articles/add/', create_article),
    # path('article/', article_view)
]