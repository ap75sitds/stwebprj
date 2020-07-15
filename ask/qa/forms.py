#from django import forms
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Question, Answer 

class SignUpForm(ModelForm):
    username  = forms.CharField(max_length=100, label="username")
    email = forms.EmailField(max_length=254,label="email", help_text='Required Field')
    password = forms.CharField(label="password",
    widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username','email','password')

class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']