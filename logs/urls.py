
from django.urls import path
from logs import views

app_name = "logs"

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('resources/', views.resources, name='resources'),
    path('new_topic/', views.new_topic, name="new_topic"),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]

