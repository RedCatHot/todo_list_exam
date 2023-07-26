from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from ToDo.models import Tag, Task


@login_required
def index(request):
    num_tags = Tag.objects.count()
    num_tasks = Task.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tags": num_tags,
        "num_tasks": num_tasks,
        "num_visits": num_visits + 1,
    }

    return render(request, "ToDo/index.html", context=context)


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    paginate_by = 3


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 3


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("ToDo:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("ToDo:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("ToDo:task-list")


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("ToDo:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("ToDo:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("ToDo:tag-list")


@login_required
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = True
    task.save()
    return redirect(reverse("ToDo:task-detail", args=[pk]))


@login_required
def undo_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = False
    task.save()
    return redirect(reverse("ToDo:task-detail", args=[pk]))
