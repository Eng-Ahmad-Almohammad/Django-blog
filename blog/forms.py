from django import forms

from .models import Comment
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