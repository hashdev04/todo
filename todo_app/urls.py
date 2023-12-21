from django.urls import path
from . import views

urlpatterns = [
    # CRUD url patterns for Todo Lists
    path('', views.list_todos, name="index"), # list
    path('list/add', views.ListCreate.as_view(), name='list-add'), # create
    path('list/<int:pk>/delete', views.ListDelete.as_view(), name='list-delete'), # delete

    # CRUD url patterns for Todo List Items
    path('list/<int:list_id>/', views.get_todo_items, name="list"), # list
    path('list/<int:list_id>/item/add', views.ItemCreate.as_view(), name='item-add'), # create
    path('list/<int:list_id>/item/<int:pk>', views.ItemUpdate.as_view(), name='item-update'), # update
    path('list/<int:list_id>/item/<int:pk>/delete', views.ItemDelete.as_view(), name='item-delete') # delete
]