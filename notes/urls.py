from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),

    path('notes/', views.notes, name='notes'),
    path('notes', views.notes, name='notes'),
    path('note_details/<int:nid>/', views.note_details, name='note_details'),
    path('note_delete/<int:did>/', views.note_delete, name='note_delete'),
    path('note_delete/<int:did>', views.note_delete, name='note_delete'),

    path('homework/', views.homework, name='homework'),
    path('homework', views.homework, name='homework'),
    path('homework_delete/<int:did>/', views.homework_delete, name='homework_delete'),

    path('youtube/', views.youtube, name='youtube'),
    path('youtube', views.youtube, name='youtube'),

    path('todo/', views.todo, name='todo'),
    path('todo', views.todo, name='todo'),
    path('todo_delete/<int:did>/', views.todo_delete, name='todo_delete'),

    path('wiki/', views.wiki, name='wiki'),
    path('wiki', views.wiki, name='wiki'),
]

