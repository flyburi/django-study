from django import forms

from .models import Post, Comment, Guestbook

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text',)

class GuestbookForm(forms.ModelForm):
    class Meta:
        model = Guestbook
        fields= ('author','text',)
