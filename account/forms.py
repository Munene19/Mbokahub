from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from account.models import User


class EmployeeRegistrationForm(UserCreationForm):


    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        self.fields['gender'].required = True
        self.fields['first_name'].label = "First Name :"
        self.fields['last_name'].label = "Last Name :"
        self.fields['password1'].label = "Password :"
        self.fields['password2'].label = "Confirm Password :"
        self.fields['email'].label = "Email :"
        self.fields['gender'].label = "Gender :"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

    class Meta:

        model=User

        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'gender']

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")
        return gender

    def save(self, commit=True):
        user = UserCreationForm.save(self,commit=False)
        user.role = "employee"
        if commit:
            user.save()
        return user
