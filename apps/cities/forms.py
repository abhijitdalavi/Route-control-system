# -*- encoding:utf-8 -*-
from django import forms
from django_select2.forms import ModelSelect2Widget, Select2Widget

from .models import DepartmentColombia, CitiesColombia


def departamento_widget():
    departamento = forms.ModelChoiceField(
        widget=Select2Widget(),
        queryset=DepartmentColombia.objects.all(),
        required=False,
    )
    return departamento


def ciudad_widget():
    ciudad = forms.ModelChoiceField(
        queryset=CitiesColombia.objects.all(),
        label="Ciudad",
        widget=ModelSelect2Widget(
            search_fields=['name__icontains'],
            dependent_fields={'departamento': 'department'},
            max_results=500,
            attrs={'class': 'form-control'},
        )
    )
    return ciudad


class UploadFileForm(forms.Form):
    file = forms.FileField()
