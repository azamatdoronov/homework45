from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from webapp.models import Sketchpad, STATUS_CHOICES


def index_view(request):
    sketchpads = Sketchpad.objects.order_by("date_of_completion")
    context = {"sketchpads": sketchpads}
    return render(request, "index.html", context)


def create_sketchpad(request):
    if request.method == "GET":
        return render(request, "create.html", {"statuses": STATUS_CHOICES})
    else:
        title = request.POST.get("title")
        description = request.POST.get("description")
        status = request.POST.get("status")
        date_of_completion = request.POST.get("date_of_completion")
        if date_of_completion == '':
            date_of_completion = None
            new_sketchpad = Sketchpad.objects.create(title=title, description=description, status=status, date_of_completion=date_of_completion)
            return redirect("sketchpad_view", pk=new_sketchpad.pk)
        else:
            new_sketchpad = Sketchpad.objects.create(title=title, description=description, status=status,date_of_completion=date_of_completion)
            return redirect("sketchpad_view", pk=new_sketchpad.pk)


def sketchpad_view(request, **kwargs):
    pk = kwargs.get("pk")
    sketchpad = get_object_or_404(Sketchpad, pk=pk)
    return render(request, "sketchpad_view.html", {"sketchpad": sketchpad})