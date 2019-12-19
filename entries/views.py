from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.template.loader import render_to_string
from django.http import JsonResponse,HttpResponseRedirect
from .models import Entry,Comment
from .forms import CommentForm
# Create your views here.
class HomeView(LoginRequiredMixin,ListView):
    model=Entry
    template_name='entries/index.html'
    context_object_name="blog_entries"
    ordering=['-entry_date']
    paginate_by=3
    #for q in Entry.objects.filter(id__exact=8) :
    #    print(q.image.url)
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
    fields=["entry_title","entry_text","restrict_comment"]
    def form_valid(self, form):
        form.instance.entry_author=self.request.user
        return super().form_valid(form)
class UpdateEntryView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Entry
    template_name="entries/create_entry.html"
    fields=["entry_title","entry_text","restrict_comment"]
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
def like_post(request):
    obj=get_object_or_404(Entry,id=request.POST.get('id'))
    user=request.user
    if user.is_authenticated:
        if user in obj.dislikes.all():
            obj.dislikes.remove(user)
            obj.likes.add(user)
        elif user in obj.likes.all():
            obj.likes.remove(user)
        else:
            obj.likes.add(user)
    context={'object':obj,}
    if request.is_ajax():
        html=render_to_string('entries/like_section.html',context,request=request)
        return JsonResponse({'form':html})
def dislike_post(request):
    obj=get_object_or_404(Entry,id=request.POST.get('id'))
    user=request.user
    if user.is_authenticated:
        if user in obj.likes.all():
            obj.likes.remove(user)
            obj.dislikes.add(user)
        elif user in obj.dislikes.all():
            obj.dislikes.remove(user)
        else:
            obj.dislikes.add(user)
    context={'object':obj,}
    if request.is_ajax():
        html=render_to_string('entries/like_section.html',context,request=request)
        return JsonResponse({'form':html})
def post_detail(request,pk):
    obj=get_object_or_404(Entry,id=pk)
    comments=Comment.objects.filter(entry=obj,reply=None).order_by('-id')
    comment_form=CommentForm(request.POST or None)
    if request.method=="POST":
        if comment_form.is_valid():
            content=request.POST.get('content')
            reply_id=request.POST.get('comment_id')
            comment_qs=None
            if reply_id:
                comment_qs=Comment.objects.get(id=reply_id)

            comment=Comment.objects.create(entry=obj,user=request.user,content=content,reply=comment_qs)
            comment.save()
        else:
            comment_form=CommentForm()
    context={
    'object':obj,
    'comments':comments,
    'comment_form':comment_form,
    }
    if request.is_ajax():
        html=render_to_string('entries/comment.html',context,request=request)
        return JsonResponse({'form':html})
    return render(request,'entries/entry_detail.html',context)
def post_delete(request,pk):
    obj=get_object_or_404(Entry,id=pk)
    obj.delete()
    return redirect('blog-home')
