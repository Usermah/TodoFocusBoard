from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, TaskForm
from .models import Task

# in views.py (temporarily)

from django.http import HttpResponse
from django.contrib.auth.models import User


# 🧑‍ Register
def register_view(request):
    if request.user.is_authenticated:
        return redirect('task-list')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task-list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# 🔐 Login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('task-list')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('task-list')
        else:
            messages.info(request, 'Invalid username or password.')

    return render(request, 'login.html')

# 🚪 Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# ✅ Task List (User-specific)
@login_required
def task_list_view(request):
    tasks = Task.objects.filter(user=request.user)
    # tasks = Task.objects.all().order_by('completed', '-id')  # uncompleted first
    return render(request, 'task_list.html', {'tasks': tasks})

# ➕ Add Task
@login_required
def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

# ✏️ Edit Task
@login_required
def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

# ❌ Delete Task
@login_required
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'task_confirm_delete.html', {'task': task})


def about_view(request):
    return render(request, 'about.html')




def create_superuser(request):
    if User.objects.filter(username='usama').exists():
        return HttpResponse("Superuser already exists")

    User.objects.create_superuser(
        username='usama',
        email='usama@gmail.com',
        password='usamaH@737!'
    )
    return HttpResponse("Superuser created successfully")






















# from django.shortcuts import redirect
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth import login
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
# from django.contrib.auth.forms import AuthenticationForm
# from django.urls import reverse_lazy
# from .models import Task
# from .forms import TaskForm, CustomUserCreationForm
# from django.contrib.auth.mixins import LoginRequiredMixin

# # 👤 Register View
# class RegisterPage(FormView):
#     template_name = 'todo_app/register.html'
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('task-list')

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return super().form_valid(form)

# # 🔐 Login View
# class CustomLoginView(LoginView):
#     template_name = 'todo_app/login.html'
#     redirect_authenticated_user = True

# # 🚪 Logout is handled by LogoutView in urls.py

# # ✅ Task List View
# class TaskListView(LoginRequiredMixin, ListView):
#     model = Task
#     context_object_name = 'tasks'
#     template_name = 'todo_app/task_list.html'

#     def get_queryset(self):
#         return Task.objects.filter(user=self.request.user)

# # ➕ Task Create View
# class TaskCreateView(LoginRequiredMixin, CreateView):
#     model = Task
#     form_class = TaskForm
#     success_url = reverse_lazy('task-list')
#     template_name = 'todo_app/task_form.html'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

# # ✏️ Task Update View
# class TaskUpdateView(LoginRequiredMixin, UpdateView):
#     model = Task
#     form_class = TaskForm
#     success_url = reverse_lazy('task-list')
#     template_name = 'todo_app/task_form.html'

# # ❌ Task Delete View
# class TaskDeleteView(LoginRequiredMixin, DeleteView):
#     model = Task
#     context_object_name = 'task'
#     success_url = reverse_lazy('task-list')
#     template_name = 'todo_app/task_confirm_delete.html'
