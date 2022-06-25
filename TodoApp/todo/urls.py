from turtle import update
from django.urls import path
from .views import TodoAppCreateView, TodoAppDeleteView, TodoAppListView, TodoAppDetailView, TodoAppUpdateView


urlpatterns = [
    path('', TodoAppCreateView.as_view(), name='home'),
    path('list/', TodoAppListView.as_view()),
    path('detail/<int:pk>/', TodoAppDetailView.as_view()),
    path('<int:pk>/update', TodoAppUpdateView.as_view()),
    path('delete/<int:pk', TodoAppDeleteView.as_view())
]
