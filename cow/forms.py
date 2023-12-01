from django import forms
from .models import cow_info_model
from django.contrib.auth.models import User


class signupform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','email')



class cow_info_form(forms.ModelForm):
    class Meta:
        model = cow_info_model
        fields = '__all__'


    def clean_name(self):
        inputname = self.cleaned_data['name']
        if inputname.isalpha()==True:
            return inputname
        else:
            raise forms.ValidationError('Numbers and special symbol are not allowed')

    def clean_milk(self):
        inputmilk =self.cleaned_data['milk']
        if inputmilk < 0:
            raise forms.ValidationError('Zero and less than zero value are not applicable')
        else:
            return inputmilk

    def clean_color(self):
        inputcolor = self.cleaned_data['color']

        if inputcolor.lower() in ['black','white','brown']:
            return inputcolor
        else:
            raise forms.ValidationError('Pease insert proper color')