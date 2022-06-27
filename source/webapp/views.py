from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

from webapp.models import Task, STATUS_CHOICES


def index_view(request):
    tasks = Task.objects.order_by("-created_task")
    context = {"tasks": tasks}
    return render(request, "index.html", context)


def task_view(request, **kwargs):
    pk = kwargs.get("pk")
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task_view.html", {"task": task})


def add_task(request):
    if request.method == "GET":
        return render(request, "add_task.html", {"statuses": STATUS_CHOICES})
    else:
        title = request.POST.get("title")
        description = request.POST.get("description")
        status = request.POST.get("status")
        dead_line = request.POST.get("dead_line")
        if dead_line == '':
            dead_line = None
            new_task = Task.objects.create(title=title, description=description, dead_line=dead_line, status=status)
            # context = {"task": new_task}
            # return render(request, "task_view.html", context)
            return redirect("task_view.html", pk=new_task.pk)
        else:
            new_task = Task.objects.create(title=title, description=description, dead_line=dead_line, status=status)
            # context = {"task": new_task}
            # return render(request, "task_view.html", context)
            return redirect("task_view.html", pk=new_task.pk)
