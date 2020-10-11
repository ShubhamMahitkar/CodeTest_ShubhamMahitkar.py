from appone.models import RegistrationModel
from django import forms


class RegistrationForm(forms.ModelForm):
    gen = (
        ('MALE', 'male'),
           ('FEMALE', 'female'),
           )
    gender = forms.ChoiceField(choices=gen, widget=forms.RadioSelect)

    class Meta:
        model = RegistrationModel
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'