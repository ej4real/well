from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from . import models
from profileacc.models import DocProfile


class DocProfileAdminCreationForm(forms.ModelForm):

    class Meta:
        model = DocProfile
        fields = ('address1', 'birth_date',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(DocProfileAdminCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class DocProfileAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    class Meta:
        model = DocProfile
        fields = ('address1', 'birth_date')

class ProfileRegForm(forms.ModelForm):

    class Meta:
        model = DocProfile
        fields = ('address1', 'birth_date')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user_obj = super(ProfileRegForm, self).save(commit=False)
        if commit:
            user_obj.save()
        return user_obj
