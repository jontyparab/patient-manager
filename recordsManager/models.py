from django.db import models

# Create your models here.
from django.urls import reverse


class PatientRecord(models.Model):
    GenderOptions = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=GenderOptions, max_length=10)
    age = models.PositiveSmallIntegerField()
    disease = models.TextField()
    doctor_name = models.CharField(max_length=200)
    doctor_fees= models.PositiveIntegerField(default=500)
    meds_started = models.DateField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('allrecords')

    class Meta:
        verbose_name = "Patient's record"