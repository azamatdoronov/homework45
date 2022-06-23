from django.shortcuts import render

# Create your views here.

from webapp.models import Task, STATUS_CHOICES


def index_view(request):
    tasks = Task.objects.order_by("-created_task")
    context = {"tasks": tasks}
    return render(request, "index.html", context)


def task_view(request):
    pk = request.GET.get("pk")
    task = Task.objects.get(pk=pk)
    return render(request, "task_view.html", {"task": task})


def add_task(request):
    if request.method == "GET":
        return render(request, "add_task.html", {"statuses": STATUS_CHOICES})
    else:
        description = request.POST.get("description")
        dead_line = request.POST.get("dead_line")
        status = request.POST.get("status")
        new_task = Task.objects.create(description=description, dead_line=dead_line, status=status)
        context = {"task": new_task}
        return render(request, 'task_view.html', context)
