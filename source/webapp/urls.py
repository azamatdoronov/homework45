from django.urls import path

from webapp.views import index_view, add_task

urlpatterns = [
    path('', index_view),
    path('tasks/add/', add_task),
    # path('task/', article_view)
]