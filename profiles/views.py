from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import ProfileForm
from .models import Profile


class ProfileList(ListView):
    model = Profile
    paginate_by = 5

    context_object_name = 'objects'


class ProfileDetail(DetailView):
    model = Profile
    


class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm


    success_url = reverse_lazy('profiles:all')


class ProfileDelete(DeleteView):
    model = Profile
    template_name = 'profiles/profile_delete.html'
    success_url = reverse_lazy('profiles:all')
