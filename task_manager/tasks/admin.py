from django.contrib import admin

from task_manager.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'author', 'executor', 'created_at')
    
    list_display_links = ('id', 'name')
    
    list_filter = ('status', 'executor', 'labels')
    
    search_fields = ('name', 'description')
    
    date_hierarchy = 'created_at'
    
    list_per_page = 25