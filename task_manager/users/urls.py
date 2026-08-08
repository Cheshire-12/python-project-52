from django.urls import path

from . import views

urlpatterns = [
    # GET /users/
    path('', views.UserListView.as_view(),
        name='users'),
    # GET /users/create/ & POST /users/create/
    path('create/', views.UserCreateView.as_view(),
        name='user_create'),
    # GET /users/<int:pk>/update/ & POST /users/<int:pk>/update/
    path('<int:pk>/update/', views.UserUpdateView.as_view(),
        name='user_update'),
    # GET /users/<int:pk>/delete/ & POST /users/<int:pk>/delete/
    path('<int:pk>/delete/', views.UserDeleteView.as_view(),
        name='user_delete'),
]