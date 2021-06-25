from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views import View

from .models import PatientRecord
from .forms import AddPatientForm


# Create your views here.

class AddPatient(CreateView):
    model = PatientRecord
    form_class = AddPatientForm
    # template_name = 'recordsManager/patientrecord_form.html'


class UpdatePatient(UpdateView):
    model = PatientRecord
    form_class = AddPatientForm
    template_name_suffix = '_update_form'
    # template_name = 'recordsManager/patientrecord_update_form.html'


class DeletePatient(DeleteView):
    model = PatientRecord
    form_class = AddPatientForm
    success_url = reverse_lazy('allrecords')
    # template_name = 'recordsManager/patientrecord_confirm_delete.html'


class AllRecords(ListView):
    model = PatientRecord
    # paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
