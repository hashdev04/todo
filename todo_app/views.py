from django.shortcuts import render
from django.views.generic import ListView
from todo_app.models import TodoList, TodoListItem
from django.http import HttpResponse

# Create your views here.

# function based view
def list_todos(request):
    todos = TodoList.objects.all()
    return render(request, 'todo_app/index.html', {'todos': todos})

# A class based view
# class ListListView(ListView):
#     model = TodoList
#     template_name = 'todo_app/index.html'

def get_todo_items(request, list_id):
    todo = TodoList.objects.get(id=list_id)
    items = TodoListItem.objects.filter(todo_list_id=list_id)
    return render(request, 'todo_app/todo_list.html', {'todo': todo, 'items': items})

# class ItemListView(ListView):
#     model = TodoListItem
#     template_name = 'todo_app/todo_list.html'

#     def get_queryset(self):
#         return TodoListItem.objects.filter(todo_list_id=self.kwargs['list_id'])
    
#     def get_context_data(self):
#         context = super().get_context_data()
#         context['todo_list'] = TodoList.objects.get(id=self.kwargs['list_id'])
#         return context
