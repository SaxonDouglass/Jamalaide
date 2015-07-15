from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, resolve_url
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.utils.http import is_safe_url
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from accounts.models import Profile
from jams.models import Game

@login_required
def profile(request):
    games = Game.objects.filter(creators=request.user)
    return render_to_response('accounts/profile.html',{ 'profile': request.user.profile, 'games': games },
                              context_instance=RequestContext(request))

class ProfileForm(forms.ModelForm):
    email_address = forms.EmailField(required=True)
    
    class Meta:
        model=Profile
        fields = ('name', 'email_address', 'show_email', 'image', 'brief', 'extended')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        if "instance" in kwargs:
            self.fields["email_address"].initial = kwargs["instance"].user.email

    def save(self, user=None, commit=True):
        profile = super(ProfileForm, self).save(commit=False)

        if user:
            user.email = self.cleaned_data["email_address"]
            user.save()
            profile.user = user
        else:
            profile.user.email = self.cleaned_data["email_address"]
        if commit:
            profile.save()
        return profile

@login_required
def update(request):
    if request.method =='POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save()
            return HttpResponseRedirect('/accounts/profile/')
    else:
        form = ProfileForm(instance=request.user.profile)

    context = {
        'form': form,
    }

    return render_to_response('accounts/update.html', context,
                              context_instance=RequestContext(request))

def register(request):
    redirect_field_name = 'next'
    redirect_to = request.POST.get(redirect_field_name, request.GET.get(redirect_field_name, ''))

    if not is_safe_url(url=redirect_to, host=request.get_host()):
        redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

    if request.user.is_authenticated():
        return HttpResponseRedirect(redirect_to)
    
    if request.method =='POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(user=user)

            user = authenticate(username=request.POST['username'],
                                password=request.POST['password1'])
            login(request, user)

            return HttpResponseRedirect(redirect_to)
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        redirect_field_name: redirect_to,
    }

    return render_to_response('accounts/register.html', context,
                              context_instance=RequestContext(request))
