from typing import Any
from django import forms
from app.models import *
from app.views import *
from django.core.validators import MinLengthValidator,RegexValidator,MaxLengthValidator  # THIS IMPORTING IS FOR BUILT-IN VALIDATORS.

def validate_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('should not starts with a')
    

def validate_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('length should  be more than 5')

class TopicForm(forms.Form):
    topic_name=forms.CharField(validators=[validate_for_a,validate_for_len])
    mobilenumber=forms.CharField(min_length=10,max_length=10,validators=[RegexValidator('[6-9]\d{9}')])  # BUILT-IN VALIDATORS

def validate_for_url(value):
    if value.endswith('.in'):
        raise forms.ValidationError('please  check ')
    
def validate_for_len(value):
    if len(value)<3:
        raise forms.ValidationError('length should  be more than 10')

    

class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField()
    url=forms.URLField(validators=[validate_for_url])
    email=forms.EmailField()

    # FORM CLASS OBJECT METHODS
    
    reemail=forms.CharField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)

    def clean(self):
        email=self.cleaned_data['email']
        reemail=self.cleaned_data['reemail']
        if email!=reemail:
            raise forms.ValidationError('chech the email')


    def clean_url(self):
        cu=self.cleaned_data['url']
        if cu[-1]=='in':
            raise forms.ValidationError('ended with .in')


 

class AccessRecordForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Topic.objects.all())
    date=forms.DateField()
    author=forms.CharField()