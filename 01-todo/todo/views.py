from django.shortcuts import render, redirect
from .models import Todo


def todo_list(request):
    if request.method == "POST":
        action = request.POST.get("action", "create")

        if action == "create":
            # 从顶部表单创建新的 Todo
            title = request.POST.get("title", "").strip()
            description = request.POST.get("description", "").strip()
            if title:
                Todo.objects.create(
                    title=title,
                    description=description,
                    is_completed=False,
                )

        elif action == "toggle":
            # 切换完成状态
            todo_id = request.POST.get("todo_id")
            if todo_id:
                try:
                    todo = Todo.objects.get(pk=todo_id)
                    todo.is_completed = not todo.is_completed
                    todo.save()
                except Todo.DoesNotExist:
                    pass

        elif action == "delete":
            # 删除任务
            todo_id = request.POST.get("todo_id")
            if todo_id:
                Todo.objects.filter(pk=todo_id).delete()

        # 所有 POST 操作完成后，重定向回列表，避免刷新重复提交
        return redirect("todo_list")

    # GET 请求：正常显示列表
    todos = Todo.objects.all().order_by("-created_at")
    return render(request, "todo/todo_list.html", {"todos": todos})
