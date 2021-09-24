from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Comment


#post comment form
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email', 'body')
        widgets = {
            'name': TextInput(attrs={
                'class': "w-full px-3 py-2 pt-5 pb-2 border border-gray-200 rounded appearance-none input focus focus:border-indigo-600 focus:outline-none active:outline-none active:border-indigo-600",
                
                'placeholder': 'Name'
                }),
            'email': EmailInput(attrs={
                'class': "w-full px-3 py-3 pt-5 pb-2 border border-gray-200 rounded appearance-none input focus focus:border-indigo-600 focus:outline-none active:outline-none active:border-indigo-600", 
                
                'placeholder': 'Email'
                }),
            'body': Textarea(attrs={
                'class': "w-full px-4 py-3 mb-4 border border-2 border-transparent border-gray-200 rounded-lg focus:ring focus:ring-blue-500 focus:outline-none", 
                
                'placeholder': 'Write your comment here'
                })
        }




        