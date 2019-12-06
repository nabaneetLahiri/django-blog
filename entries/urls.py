

from django.urls import path
from .views import HomeView,EntryView,CreateEntryView,UpdateEntryView,DeleteEntryView
urlpatterns = [
path('',HomeView.as_view(),name='blog-home'),
path('entry/<int:pk>/',EntryView.as_view(),name="entry-detail"),
path('entry/<int:pk>/update',UpdateEntryView.as_view(success_url='/'),name="entry-update"),
path('entry/<int:pk>/delete',DeleteEntryView.as_view(success_url='/'),name="entry-delete"),
path('create_entry/',CreateEntryView.as_view(success_url='/'),name='create_entry')
]
