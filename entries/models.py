from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
"""
import cloudinary
import cloudinary.uploader
import cloudinary.api
"""
# Create your models here.
def upload_location(instance,filename):
    return "%s/%s" %(instance.id,filename)
class Entry(models.Model):
    entry_title=models.CharField(max_length=50,verbose_name= ('Title'))
    entry_text=RichTextUploadingField(blank=True,null=True,verbose_name= ('Text'))
    entry_date=models.DateTimeField(auto_now_add=True)
    entry_author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,blank=True,related_name="post_likes")
    dislikes=models.ManyToManyField(User,blank=True,related_name="post_dislikes")
    restrict_comment=models.BooleanField(default=False)
    class Meta:
        verbose_name_plural="entries"
    def __str__(self):
        return f'{self.entry_title}'
    def total_likes(self):
        return likes.count()
    def get_absolute_url(self):
        return f"/entry/{self.id}/"
class Comment(models.Model):
    entry=models.ForeignKey(Entry,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    reply=models.ForeignKey('self',null=True,related_name='replies',on_delete=models.CASCADE)
    content=models.TextField(max_length=160)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.entry.entry_title}-{str(self.user.username)}'
