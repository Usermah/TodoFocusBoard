from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.task_list_view, name='task-list'),
    path('task/create/', views.task_create_view, name='task-create'),
    path('task/<int:pk>/edit/', views.task_update_view, name='task-edit'),
    path('task/<int:pk>/delete/', views.task_delete_view, name='task-delete'),

    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('about/', views.about_view, name='about'),

    path('createsuperuser/', views.create_superuser, name='create-superuser'),  # TEMPORARY
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
