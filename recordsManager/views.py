from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views import View

from .models import PatientRecord
from .forms import AddPatientForm


# Create your views here.

class AddPatient(CreateView):
    model = PatientRecord
    form_class = AddPatientForm
    def get_success_url(self):
        messages.success(self.request, "New Record Added")
        return reverse('recordsManager:allrecords')


class UpdatePatient(UpdateView):
    model = PatientRecord
    form_class = AddPatientForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        messages.info(self.request, "Record Updated")
        return reverse('recordsManager:allrecords')


class DeletePatient(DeleteView):
    model = PatientRecord
    form_class = AddPatientForm
    def get_success_url(self):
        messages.error(self.request, "Record Deleted")
        return reverse('recordsManager:allrecords')
    

class AllRecords(ListView):
    model = PatientRecord
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
