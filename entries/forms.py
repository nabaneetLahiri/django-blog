from django import forms
from .models import Comment
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Comments...','style':'width:100%; height:100px;'}))
    class Meta:
        model=Comment
        fields={'content'}
    """
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = "Your Comment"
    """
