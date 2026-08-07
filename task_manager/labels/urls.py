from django.urls import path
from . import views

app_name = 'labels'

urlpatterns = [
    # GET /labels/
    path('', views.LabelIndexView.as_view(), name='list'),
    # GET /labels/create/ & POST /labels/create/
    path('create/', views.LabelCreateView.as_view(), name='create'),
    # GET /labels/<int:pk>/update/ & POST /labels/<int:pk>/update/
    path('<int:pk>/update/', views.LabelUpdateView.as_view(), name='update'),
    # GET /labels/<int:pk>/delete/ & POST /labels/<int:pk>/delete/
    path('<int:pk>/delete/', views.LabelDeleteView.as_view(), name='delete'),
]