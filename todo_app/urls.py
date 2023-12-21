from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_todos, name="index"),
    path('list/<int:list_id>/', views.get_todo_items, name="list"),
    
    # CRUD
    path('list/add', views.ListCreate.as_view(), name='list-add'),
    path('list/<int:list_id>/item/add', views.ItemCreate.as_view(), name='item-add'),
    path('list/<int:list_id>/item/<int:pk>', views.ItemUpdate.as_view(), name='item-update')
]