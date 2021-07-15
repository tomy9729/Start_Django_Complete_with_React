from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import fields
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address','zipcode']

class LoginFrom(AuthenticationForm) : 
    answer = forms.IntegerField(help_text="9 x 9 = ?")

    def clean_answer(self ) : 
        answer = self.cleaned_data.get('answer')
        if answer != 81 : 
            raise forms.ValidationError("틀렸습니다.")
        return answer
