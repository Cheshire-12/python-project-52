from django.urls import path
from . import views

app_name = 'statuses'

urlpatterns = [
    # GET /statuses/
    path('', views.StatusIndexView.as_view(), name='list'),
    # GET /statuses/create/ & POST /statuses/create/
    path('create/', views.StatusCreateView.as_view(), name='create'),
    # GET /statuses/<int:pk>/update/ & POST /statuses/<int:pk>/update/
    path('<int:pk>/update/', views.StatusUpdateView.as_view(), name='update'),
    # GET /statuses/<int:pk>/delete/ & POST /statuses/<int:pk>/delete/
    path('<int:pk>/delete/', views.StatusDeleteView.as_view(), name='delete'),
]