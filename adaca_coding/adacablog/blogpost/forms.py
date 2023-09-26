from django import forms
from .views import BlogPost

class CreateNewPost(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title of your post', 'style':'width: 300px;' 
                                                          'border:1px solid black;' 'margin-bottom:20px;''margin-left:15px;'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Share your thoughts!', 'style':'width: 300px;' 
                                                           'border:1px solid black;'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Author Name', 'style':'width: 300px;' 
                                                          'border:1px solid black;'}))
