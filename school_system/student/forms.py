from django import forms
from .models import Student
class StudentRegistrationForm(forms.ModelForm):
    class Meta():
        model=Student
        fields=("__all__")
        widgets={
            '__all__':forms.TextInput(attrs={'class':'form-control'})
        }

        