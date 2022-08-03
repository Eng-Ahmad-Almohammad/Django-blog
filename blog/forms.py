from django import forms

from .models import Comment, Post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__( *args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'input'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['class'] = 'input'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['body'].widget.attrs['class'] = 'input'
        self.fields['body'].widget.attrs['placeholder'] = 'Leave a Comment'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ['title', 'intro', 'body', 'status', 'image', 'category']
        exclude = ['slug', 'created_at', 'author']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['class'] = "input"
        self.fields['title'].widget.attrs['class'] = "input"
        self.fields['title'].widget.attrs['placeholder'] = "Post Title"
        self.fields['intro'].widget.attrs['class'] = "input"
        self.fields['intro'].widget.attrs['placeholder'] = "Intro for the post"
        self.fields['body'].widget.attrs['class'] = "input"
        self.fields['body'].widget.attrs['placeholder'] = "Body of the post"
        self.fields['status'].widget.attrs['class'] = "input"
        self.fields['image'].widget.attrs['class'] = "input"