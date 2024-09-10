from django import forms
from .models import Comment

class ContactForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))    


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        body = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control'}))
    