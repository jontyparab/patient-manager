from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import PatientRecord
from .forms import AddPatientForm


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
    # Newer Records should be shown first
    ordering = ['-created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
