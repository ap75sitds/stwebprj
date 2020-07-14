#from django import forms
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Question, Answer 

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required Field')
    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2',)

class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']