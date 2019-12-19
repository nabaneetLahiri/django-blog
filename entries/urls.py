

from django.urls import path
from .views import HomeView,MyView,EntryView,CreateEntryView,UpdateEntryView,DeleteEntryView
from . import views
urlpatterns = [
path('',HomeView.as_view(),name='blog-home'),
path('account/',MyView.as_view(),name='my-entry'),
#path('entry/<int:pk>/',EntryView.as_view(),name="entry-detail"),
path('entry/<int:pk>/',views.post_detail,name="detail"),
path('entry/<int:pk>/update',UpdateEntryView.as_view(success_url='/'),name="entry-update"),
#path('entry/<int:pk>/delete',DeleteEntryView.as_view(success_url='/'),name="entry-delete"),
path('entry/<int:pk>/delete',views.post_delete,name="delete"),
path('entry/like',views.like_post,name="like_post"),
path('entry/dislike',views.dislike_post,name="dislike_post"),
path('create_entry/',CreateEntryView.as_view(success_url='/'),name='create_entry')

]
