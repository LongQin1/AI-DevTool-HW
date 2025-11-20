# Homework 1 — Introduction to AI-Assisted Development

This repository contains my solution for **Homework 1: Introduction to AI-Assisted Development** from the AI Dev Tools Zoomcamp.

The goal of this homework is to build a small **Django TODO application** with the help of an AI assistant (e.g. ChatGPT, Copilot, etc.), and to practice using AI for step-by-step coding support, debugging and setup.

All code for this homework lives in the folder:

- 01-todo/


## Project Structure

Repository root:

- 01-todo/
    - manage.py
    - todo_project/  (Django project)
    - todo/          (Django app implementing the TODO functionality)


## Tech Stack

- Python
- Django
- HTML + CSS (custom, no frontend framework)
- Git + GitHub for version control
- AI assistant (ChatGPT) for guidance and code generation


## How to Run the Project Locally

From the repository root:

    cd 01-todo

Create and activate a virtual environment (Windows / PowerShell):

    python -m venv .venv
    .venv\Scripts\activate

Install Django:

    pip install django

Apply migrations:

    python manage.py migrate

Run the development server:

    python manage.py runserver

Then open in your browser:

- Main TODO app (purple UI):  http://127.0.0.1:8000/
- Django admin (optional):    http://127.0.0.1:8000/admin/


## Django App Details

Project name:  todo_project  
App name:      todo


### Models

File: `todo/models.py`

    from django.db import models

    class Todo(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField(blank=True)
        is_completed = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title

The `Todo` model includes:

- `title` — short title of the task  
- `description` — optional longer description  
- `is_completed` — boolean flag for completion  
- `created_at` — timestamp when the task was created  


### Admin

File: `todo/admin.py`

The `Todo` model is registered in Django admin so tasks can be created, viewed and edited from the admin UI if needed.


### Views

File: `todo/views.py`

The main view is `todo_list`, which:

- On **GET**:
    - Retrieves all todos, ordered by `created_at` descending.
    - Renders the main template `todo/todo_list.html`.

- On **POST**:
    - Handles creating a new task.
    - Handles toggling a task as **Done / Undo**.
    - Handles deleting a task.

This makes the frontend page fully interactive (create + complete + delete) without relying only on the admin page.


### URLs

Project URLs: `todo_project/urls.py`

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('todo.urls')),
    ]

App URLs: `todo/urls.py`

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.todo_list, name='todo_list'),
    ]

The root path `/` is mapped to `todo_list`, which serves the main TODO page.


### Templates / Frontend

File: `todo/templates/todo/todo_list.html`

- Custom **purple-themed** UI with a modern look.
- Responsive layout that uses more of the screen width.
- Features:
    - A form at the top to **add new tasks** (title + optional description).
    - A task list showing:
        - Title  
        - Created date  
        - Optional truncated description  
        - Status (Done / In progress)  
    - Buttons beside each task to:
        - **Done / Undo** (toggle completion state)
        - **Delete** the task
    - A small “mini dashboard” on the right-hand side (for fun / overview).


## AI-Assisted Development

For this homework, I used an AI assistant (ChatGPT) to:

- Generate step-by-step instructions for installing Python dependencies and Django.
- Help with Django project/app setup (`startproject`, `startapp`, `INSTALLED_APPS`, URLs).
- Design the `Todo` model and register it in the admin site.
- Build the HTML/CSS for a clean, purple-themed UI.
- Implement the POST handling logic to create, toggle and delete tasks from the main page.
- Guide the Git and GitHub workflow (init, commit, push).
- Double-check that I answered all homework questions correctly and followed the instructions.


## Homework Questions & Answers

Below are the required homework questions and my answers, based on what I actually did in this repository.


### Question 1: Install Django

> We want to install Django. Ask AI to help you with that.  
> What's the command you used for that?

**Answer:**

    pip install django


### Question 2: Add a new app

> Now we want to add a TODO app. Ask AI to help you with adding the app.  
> What file do you modify when you add a new app?

**Answer:**

    settings.py

Concretely, I added `"todo"` to the `INSTALLED_APPS` list in:

- `todo_project/settings.py`


### Question 3: After creating models

> Now we want to create some models. Ask AI to help you with that.  
> After creating models in Django, what should you do next?

**Answer:**

    Run migrations

The actual commands I used were:

    python manage.py makemigrations
    python manage.py migrate


### Homework URL

> Commit your code to GitHub. You can create a repository for this homework, or use an existing one.  
> In the repository, create a folder, e.g. "01-todo", where you put the code.  
> Use the link to this folder in the homework submission form.

Repository:

- https://github.com/LongQin1/AI-DevTool-HW

Homework folder URL (to submit in the form):

- https://github.com/LongQin1/AI-DevTool-HW/tree/main/01-todo
