from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import JobForm
from .models import Job


class JobList(ListView):
    model = Job
    context_object_name = 'jobs'


class JobDetail(DetailView):
    model = Job
    context_object_name = 'job'


class JobCreate(CreateView):
    model = Job
    template_name = 'jobs/job_create.html'
    form_class = JobForm
    success_url = reverse_lazy('jobs:all')


class JobUpdate(UpdateView):
    model = Job
    template_name = 'jobs/job_update.html'
    form_class = JobForm
    success_url = reverse_lazy('jobs:detail')


class JobDelete(DeleteView):
    model = Job
    template_name = 'jobs/job_delete.html'
    success_url = reverse_lazy('jobs:all')
