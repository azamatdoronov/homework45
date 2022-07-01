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
            new_sketchpad = Sketchpad.objects.create(title=title, description=description, status=status,
                                                     date_of_completion=date_of_completion)
            return redirect("sketchpad_view", pk=new_sketchpad.pk)
        else:
            new_sketchpad = Sketchpad.objects.create(title=title, description=description, status=status,
                                                     date_of_completion=date_of_completion)
            return redirect("sketchpad_view", pk=new_sketchpad.pk)


def sketchpad_view(request, **kwargs):
    pk = kwargs.get("pk")
    sketchpad = get_object_or_404(Sketchpad, pk=pk)
    return render(request, "sketchpad_view.html", {"sketchpad": sketchpad})


def update_sketchpad(request, pk):
    sketchpad = get_object_or_404(Sketchpad, pk=pk)
    if request.method == "GET":
        context = {
            "statuses": STATUS_CHOICES,
            "sketchpad": sketchpad
        }
        return render(request, "update.html", context)
    else:
        sketchpad.title = request.POST.get("title")
        sketchpad.description = request.POST.get("description")
        sketchpad.status = request.POST.get("status")
        sketchpad.date_of_completion = request.POST.get("date_of_completion")
        sketchpad.save()
        return redirect("sketchpad_view", pk=sketchpad.pk)


def delete_sketchpad(request, pk):
    sketchpad = get_object_or_404(Sketchpad, pk=pk)
    if request.method == "GET":
        pass
        # return render(request, "delete.html", {"sketchpad": sketchpad})
    else:
        sketchpad.delete()
        return redirect("index")
