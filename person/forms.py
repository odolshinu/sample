from django import forms

from .models import Person

class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    age = forms.IntegerField(label="Age", widget=forms.TextInput)

class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age']
