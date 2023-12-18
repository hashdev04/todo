from django.contrib import admin
from todo_app.models import TodoList, TodoListItem

# Register your models here.

admin.site.register(TodoList)
admin.site.register(TodoListItem)