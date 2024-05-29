from typing import Any
from django import forms

class EmployeeForm(forms.Form):
    ename=forms.CharField(max_length=25)
    eage=forms.IntegerField(max_value=100)
    email=forms.EmailField()
    sal=forms.FloatField(max_value=1000000)


    def clean_ename(self):
        data = self.cleaned_data["ename"]
        if len(data)<3:
            raise ValueError("name should be greater than 3 characters")
        
        return data
    
    def clean_eage(self):
        data=self.cleaned_data['eage']
        if not(data>=18 and data<=25):
           raise ValueError("Age should be between 18 and 25") 
        return data
    
    
