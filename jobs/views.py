from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import JobForm
from .models import Job
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class JobList(ListView):
    model = Job
    paginate_by = 5
    context_object_name = 'jobs'


class JobDetail(DetailView):
    model = Job
    context_object_name = 'job'


@method_decorator(login_required, name='dispatch')
class JobCreate(CreateView):
    model = Job
    template_name = 'jobs/job_create.html'
    form_class = JobForm

    def form_valid(self, JobForm):
        job = JobForm.save(commit=False)
        job.profile = self.request.user.profile
        return super(JobCreate, self).form_valid(JobForm)

    success_url = reverse_lazy('jobs:all')


class JobUpdate(UpdateView):
    model = Job
    template_name = 'jobs/job_update.html'
    form_class = JobForm
    success_url = reverse_lazy('jobs:all')



class JobDelete(DeleteView):
    model = Job
    template_name = 'jobs/job_delete.html'
    success_url = reverse_lazy('jobs:all')
