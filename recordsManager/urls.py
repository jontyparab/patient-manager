from django.urls import path
from . import views

app_name = 'recordsManager'

urlpatterns = [
    path('add/', views.AddPatient.as_view(), name='addpatient'),
    path('update/<int:pk>', views.UpdatePatient.as_view(), name='updpatient'),
    path('delete/<int:pk>', views.DeletePatient.as_view(), name='delpatient'),
    path('all/', views.AllRecords.as_view(), name='allrecords'),
]