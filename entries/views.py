from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Entry
# Create your views here.
class HomeView(LoginRequiredMixin,ListView):
    model=Entry
    template_name='entries/index.html'
    context_object_name="blog_entries"
    ordering=['-entry_date']
    paginate_by=3
class MyView(LoginRequiredMixin,ListView):
    model=Entry#.objects.get(entry_author__exact=.request.user)
    template_name='entries/index.html'
    context_object_name="blog_entries"
    ordering=['-entry_date']
    paginate_by=3
    def get_queryset(self):
        return Entry.objects.filter(
        entry_author__exact=self.request.user
        )
class EntryView(LoginRequiredMixin,DetailView):
    model=Entry
    template_name='entries/entry_detail.html'
class CreateEntryView(LoginRequiredMixin,CreateView):
    model=Entry
    template_name="entries/create_entry.html"
    fields=["entry_title","entry_text"]
    def form_valid(self, form):
        form.instance.entry_author=self.request.user
        return super().form_valid(form)
class UpdateEntryView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Entry
    template_name="entries/create_entry.html"
    fields=["entry_title","entry_text"]
    def form_valid(self, form):
        form.instance.entry_author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        entry=self.get_object()
        if self.request.user==entry.entry_author:
            return True
        return False
class DeleteEntryView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Entry
    template_name='entries/confirm_delete.html'
    def test_func(self):
        entry=self.get_object()
        if self.request.user==entry.entry_author:
            return True
        return False
class PostLikeView(RedirectView):
    pattern_name = 'entry-detail'
    def get_redirect_url(self, *args, **kwargs):
        obj = Entry.objects.get(pk=kwargs['pk'])
        user = self.request.user
        if user.is_authenticated:
            if user in obj.dislikes.all():
                obj.dislikes.remove(user)
                obj.likes.add(user)
            elif user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return super().get_redirect_url(*args, **kwargs)
class PostDislikeView(RedirectView):
    pattern_name = 'entry-detail'
    def get_redirect_url(self, *args, **kwargs):
        obj = Entry.objects.get(pk=kwargs['pk'])
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
                obj.dislikes.add(user)
            elif user in obj.dislikes.all():
                obj.dislikes.remove(user)
            else:
                obj.dislikes.add(user)
        return super().get_redirect_url(*args, **kwargs)
