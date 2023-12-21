from typing import Any
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from todo_app.models import TodoList, TodoListItem

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

class ListCreate(CreateView):
    model = TodoList
    fields = ['title']

    def get_context_data(self):
        context = context = super(ListCreate, self).get_context_data()
        context['title'] = 'Add a new list'
        return context

class ItemCreate(CreateView):
    model = TodoListItem
    fields = [
        'title',
        'description',
        'due_date',
        'todo_list'
    ]

    def get_initial(self):
        initial_data =  super(ItemCreate, self).get_initial()
        todo_list = TodoList.objects.get(id=self.kwargs['list_id'])
        initial_data['todo_list'] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = TodoList.objects.get(id=self.kwargs['list_id'])
        context['todo_list'] = todo_list
        context['title'] = 'Create a new item'
        return context
    
    def get_success_url(self):
        return reverse('list', args=[self.object.todo_list_id])


class ItemUpdate(UpdateView):
    model = TodoListItem
    fields = [
        'title',
        'description',
        'due_date',
        'todo_list'
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context['todo_list'] = self.object.todo_list
        context['title'] = 'Edit Item'
        return context
    
    def get_success_url(self):
        return reverse('list', args=[self.object.todo_list_id])
    