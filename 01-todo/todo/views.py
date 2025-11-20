from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo


def todo_list(request):
    if request.method == "POST":
        action = request.POST.get("action", "create")

        if action == "create":
            title = request.POST.get("title", "").strip()
            description = request.POST.get("description", "").strip()
            due_date_str = request.POST.get("due_date", "").strip()

            due_date = None
            if due_date_str:
                try:
                    due_date = date.fromisoformat(due_date_str)
                except ValueError:
                    due_date = None  
            if title:
                Todo.objects.create(
                    title=title,
                    description=description,
                    is_completed=False,
                    due_date=due_date,
                )

        elif action == "toggle":
            todo_id = request.POST.get("todo_id")
            if todo_id:
                try:
                    todo = Todo.objects.get(pk=todo_id)
                    todo.is_completed = not todo.is_completed
                    todo.save()
                except Todo.DoesNotExist:
                    pass

        elif action == "delete":
            todo_id = request.POST.get("todo_id")
            if todo_id:
                Todo.objects.filter(pk=todo_id).delete()

        return redirect("todo_list")

    todos = Todo.objects.all().order_by("-created_at")
    return render(request, "todo/todo_list.html", {"todos": todos})


def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        due_date_str = request.POST.get("due_date", "").strip()

        due_date = None
        if due_date_str:
            try:
                due_date = date.fromisoformat(due_date_str)
            except ValueError:
                due_date = None

        if title:
            todo.title = title
            todo.description = description
            todo.due_date = due_date
            todo.save()

        return redirect("todo_list")

    return render(request, "todo/edit_todo.html", {"todo": todo})
