from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    # GET /tasks/
    path('', views.TaskIndexView.as_view(), name='list'),
    # GET /tasks/create/ & POST /tasks/create/
    path('create/', views.TaskCreateView.as_view(), name='create'),
    # GET /tasks/<int:pk>/update/ & POST /tasks/<int:pk>/update/
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='update'),
    # GET /tasks/<int:pk>/delete/ & POST /tasks/<int:pk>/delete/
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete'),
    # GET /tasks/<int:pk>/
    path('<int:pk>/', views.TaskDetailView.as_view(), name='detail'),
]