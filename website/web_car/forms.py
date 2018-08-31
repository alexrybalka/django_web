from django import forms
from .models import VehiclePart, Section


class VehiclePartForm(forms.ModelForm):
    class Meta:
        model = VehiclePart
        fields = ['name', 'price', 'description', 'pub_date', 'section']


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'description']
