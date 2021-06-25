from django import forms
from .models import PatientRecord


class AddPatientForm(forms.ModelForm):
    class Meta:
        model = PatientRecord
        fields = ('first_name', 'last_name', 'gender', 'age', 'disease', 'doctor_name', 'doctor_fees', 'meds_started')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'autofocus':'true'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'disease': forms.Textarea(attrs={'class': 'form-control'}),
            'doctor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'doctor_fees': forms.NumberInput(attrs={'class': 'form-control'}),
            'meds_started': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'autocapitalize':'off'}),
        }
