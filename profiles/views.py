from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import ProfileForm
from .models import Profile


class ProfileList(ListView):
    model = Profile
    context_object_name = 'objects'


class ProfileDetail(DetailView):
    model = Profile
    context_object_name = 'object'



class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('profiles:detail')


class ProfileDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('profiles:all')
