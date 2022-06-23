from django.urls import path

from webapp.views import index_view, add_task, task_view

urlpatterns = [
    path('', index_view),
    path('tasks/add/', add_task),
    path('task/', task_view),
]