# Homework 1 — Introduction to AI-Assisted Development

This repository contains my solution for **Homework 1: Introduction to AI-Assisted Development** from the AI Dev Tools Zoomcamp.

The goal of this homework is to build a small **Django TODO application** with the help of an AI assistant (e.g. ChatGPT, Copilot, etc.), and to practice using AI for step-by-step coding support, debugging and setup.

The TODO app can:

- Create, edit and delete TODOs  
- Assign due dates  
- Mark TODOs as resolved  

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
        due_date = models.DateField(null=True, blank=True)

        def __str__(self):
            return self.title

The `Todo` model includes:

- `title` — short title of the task  
- `description` — optional longer description  
- `is_completed` — boolean flag for completion  
- `created_at` — timestamp when the task was created  
- `due_date` — optional due date for the task  


### Admin

File: `todo/admin.py`

The `Todo` model is registered in Django admin so tasks can be created, viewed and edited from the admin UI if needed.


### Views and Logic

File: `todo/views.py`

There are two main views:

1. `todo_list`  
   - On **GET**:
       - Retrieves all todos, ordered by `created_at` descending.
       - Renders the main template `todo/todo_list.html`.
   - On **POST**:
       - `action="create"`: creates a new task (title, description and optional `due_date`).
       - `action="toggle"`: toggles the `is_completed` flag (Done / Undo).
       - `action="delete"`: deletes a task.

   This makes the main page fully interactive: create, complete/undo, and delete tasks.

2. `edit_todo`  
   - Allows editing an existing task:
       - Title
       - Description
       - Due date
   - On **POST**, updates the task and redirects back to the main list.

This covers the logic for Create / Edit / Delete, assigning due dates, and marking tasks as resolved.


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
        path('edit/<int:pk>/', views.edit_todo, name='edit_todo'),
    ]

The root path `/` is mapped to `todo_list`, which serves the main TODO page.  
The path `/edit/<pk>/` serves the edit page for a specific task.


### Templates / Frontend

Main template: `todo/templates/todo/todo_list.html`  
Edit template: `todo/templates/todo/edit_todo.html`

The frontend uses a custom **purple-themed** UI with a modern look and a responsive layout that uses more of the screen width.

Features:

- A form at the top of the main page to **add new tasks**:
    - Title (required)  
    - Description (optional)  
    - Due date (optional, date input)  
- A task list showing:
    - Title  
    - Created date  
    - Due date (if present)  
    - Description (truncated)  
    - Status (Done / In progress)  
- Buttons beside each task to:
    - **Done / Undo** (toggle completion state)
    - **Delete** the task
    - **Edit** the task (opens the edit page)
- A small “mini dashboard” on the right-hand side for a quick overview.

The edit page (`edit_todo.html`) allows updating title, description and due date in a simple card-style UI that matches the main theme.


## Tests

File: `todo/tests.py`

Basic tests are implemented to make sure the core functionality works:

- Model tests:
    - Creating a `Todo` with a `due_date` stores the correct values.

- View tests:
    - Creating a Todo via POST to `todo_list` (with `action="create"`) works and sets `due_date` correctly.
    - Toggling completion via POST with `action="toggle"` correctly flips `is_completed`.
    - Deleting a Todo via POST with `action="delete"` removes it from the database.
    - Editing a Todo via POST to `edit_todo` updates title, description and `due_date`.

To run the tests, use:

    python manage.py test


## AI-Assisted Development

For this homework, I used an AI assistant (ChatGPT) to:

- Generate step-by-step instructions for installing Python dependencies and Django.
- Help with Django project/app setup (`startproject`, `startapp`, `INSTALLED_APPS`, URLs).
- Design the `Todo` model (including `due_date`) and register it in the admin site.
- Build the HTML/CSS for a clean, purple-themed UI.
- Implement the POST handling logic to create, toggle, delete and edit tasks from the main page and edit page.
- Suggest and refine unit tests for the main functionality, and debug until `python manage.py test` passes.
- Guide the Git and GitHub workflow (init, commit, push).
- Double-check that I answered all homework questions correctly and followed the instructions.


## Homework Questions & Answers

Below are the required homework questions and my answers, based on what I actually did in this repository.


### Question 1: Install Django

> We want to install Django. Ask AI to help you with that.  
> What's the command you used for that?

**Answer:**

    pip install django


### Question 2: Project and App

> Now we need to create a project and an app for that.  
> At some point, you will need to include the app you created in the project.  
> What's the file you need to edit for that?

Options: `settings.py`, `manage.py`, `urls.py`, `wsgi.py`

**Answer:**

    settings.py

Concretely, I added `"todo"` to the `INSTALLED_APPS` list in:

- `todo_project/settings.py`


### Question 3: Django Models

> Let's now proceed to creating models.  
> For the TODO app, which models do we need? Implement them.  
> What's the next step you need to take?

Options: Run the application, Add the models to the admin panel, Run migrations, Create a makefile

**Answer:**

    Run migrations

After creating the `Todo` model, I ran:

    python manage.py makemigrations
    python manage.py migrate


### Question 4: TODO Logic

> Let's now ask AI to implement the logic for the TODO app. Where do we put it?

Options: `views.py`, `urls.py`, `admin.py`, `tests.py`

**Answer:**

    views.py

All application logic for creating, editing, deleting and toggling TODOs is implemented in `todo/views.py`.


### Question 5: Templates

> Next step is creating the templates. You will need at least two: `base.html` and `home.html`.  
> Where do you need to register the directory with the templates?

Options:

- `INSTALLED_APPS` in project's `settings.py`
- `TEMPLATES['DIRS']` in project's `settings.py`
- `TEMPLATES['APP_DIRS']` in project's `settings.py`
- In the app's `urls.py`

**Answer:**

    TEMPLATES['DIRS'] in project's settings.py

Conceptually, the directory with templates is registered via the `TEMPLATES['DIRS']` setting in `todo_project/settings.py`.  
In this project, I mainly use app-level templates under `todo/templates/todo/`, which work together with Django's template loading mechanism.


### Question 6: Tests

> Now let's ask AI to cover our functionality with tests.  
> What's the command you use for running tests in the terminal?

Options:

- `pytest`
- `python manage.py test`
- `python -m django run_tests`
- `django-admin test`

**Answer:**

    python manage.py test

This runs the Django test suite, including the tests defined in `todo/tests.py`.


## Homework URL

Commit your code to GitHub. Within the repository, create a folder, e.g. "01-todo", where you put the code.

Repository:

- https://github.com/LongQin1/AI-DevTool-HW

Homework folder URL (to submit in the form):

- https://github.com/LongQin1/AI-DevTool-HW/tree/main/01-todo
