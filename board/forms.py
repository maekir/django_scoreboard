from django import forms
from django.contrib.auth.models import User
from .models import Comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, required=True)
    class Meta():
        model = Comment
        exclude = ('commenter', 'race')
