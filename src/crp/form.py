from django import forms
from .models import Create





class ApplyCreate(forms.ModelForm):
    
    class Meta:
        model = Create
        fields = ['project_name','contract_number','contract_date','contr_name']

    
