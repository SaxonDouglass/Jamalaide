from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from accounts.models import UserProfile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email_address']
            user = User.objects.create_user(username, email, password)
            profile = user.get_profile()
            profile.student_id = form.cleaned_data['student_id']
            profile.notify = form.cleaned_data['notify']
            profile.save()
            login(request,user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = RegistrationForm()
    
    c = {}
    c.update(csrf(request))
    c['form'] = form
    
    return render_to_response('accounts/register.html', c)

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email_address = forms.EmailField()
    student_id = forms.IntegerField(min_value=0, required=False)
    notify = forms.BooleanField(label="Recieve email notifications", initial=True)
