

from django.urls import path
from .views import HomeView,MyView,EntryView,CreateEntryView,UpdateEntryView,DeleteEntryView,PostLikeView,PostDislikeView
urlpatterns = [
path('',HomeView.as_view(),name='blog-home'),
path('account/',MyView.as_view(),name='my-entry'),
path('entry/<int:pk>/',EntryView.as_view(),name="entry-detail"),
path('entry/<int:pk>/update',UpdateEntryView.as_view(success_url='/'),name="entry-update"),
path('entry/<int:pk>/delete',DeleteEntryView.as_view(success_url='/'),name="entry-delete"),
path('entry/<int:pk>/like',PostLikeView.as_view(),name="entry-like"),
path('entry/<int:pk>/dislike',PostDislikeView.as_view(),name="entry-dislike"),
path('create_entry/',CreateEntryView.as_view(success_url='/'),name='create_entry')
]
