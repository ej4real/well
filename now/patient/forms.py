from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from . import models
from patient.models import PatientProfile

User = get_user_model

class PatientProfileAdminCreationForm(forms.ModelForm):

    class Meta:
        model = PatientProfile
        fields = ('name', 'email' , 'age', 'address', 'birth_date', 'gender', 'contact_number',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(PatientProfileAdminCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class PatientProfileAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    class Meta:
        model = PatientProfile
        fields = ('name', 'email' , 'age', 'address', 'birth_date', 'gender', 'contact_number',)

class PatProfileDetailChangeForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ('name', 'email' , 'age', 'address', 'birth_date', 'gender', 'contact_number',)

        def save(self, commit=True):
            # Save the provided password in hashed format
            user = super(PatProfileDetailChangeForm, self).save(commit=False)
            if commit:
                user.save()
            return user

class RegPatientForm(forms.ModelForm):
    
    class Meta:
        model = PatientProfile
        fields = ('name', 'email' , 'age', 'address', 'birth_date', 'gender', 'contact_number',)


    def clean_name(self):
        name = self.cleaned_data.get('name')
        qs = PatientProfile.objects.filter(name__iexact=name)
        if qs.exists():
            raise forms.ValidationError("Similar Entry of Name. Cannot Save")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = PatientProfile.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Cannot use this email. It's already registered")
        return email

#    def save(self, commit=True):
#        # Save the provided password in hashed format
#        user = super(RegPatientForm, self).save(commit=False)
#        if commit:

#            user.save()
#        return user
