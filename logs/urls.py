
from django.urls import path
from logs import views
from django.conf import settings

app_name = "logs"

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('resources/', views.resources, name='resources'),
    path('new_topic/', views.new_topic, name="new_topic"),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
]
