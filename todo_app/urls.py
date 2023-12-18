from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ListListView.as_view(), name="index"),
    path('', views.list_todos, name="index"),
    # path('list/<int:list_id>/', views.ItemListView.as_view(), name='list')
    path('list/<int:list_id>/', views.get_todo_items, name="list"),
]