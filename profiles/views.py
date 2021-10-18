from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from .forms import ProfileForm, UserForm
from .models import Profile
from datetime import date


class ProfileList(ListView):
    model = Profile
    paginate_by = 5

    context_object_name = 'objects'


class ProfileDetail(DetailView):
    model = Profile


def profile_update(req, slug):

    user = req.user
    profile = user.profile

    form = ProfileForm(instance=profile)
    form2 = UserForm(instance=user)
    if req.method == 'POST':

        form = ProfileForm(req.POST, req.FILES, instance=profile)
        form2 = UserForm(req.POST, req.FILES, instance=user)
        if form.is_valid() and form2.is_valid():

            user = form2.save(commit=False)
            user.save()

            profile = form.save(commit=False)
            profile.user = user
           

            profile.save()

            auth_login(req, user)

            #messages.success(req, 'updated')
            return redirect('profiles:detail', profile.slug)
        else:
            #messages.error(req, 'faild')
            return redirect('profiles:update', profile.slug)

    return render(req, 'profiles/profile_form.html', {'form': form, 'form2': form2})



class ProfileDelete(DeleteView):
    model = Profile
    template_name = 'profiles/profile_delete.html'
    success_url = reverse_lazy('profiles:all')
