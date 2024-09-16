from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    list_filter = ('completed',)
    search_fields = ('title', 'description')
