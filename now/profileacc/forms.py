from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from . import models
from profileacc.models import DocProfile

User = get_user_model()


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

class ProfileDetailChangeForm(forms.ModelForm):
    class Meta:
        model = DocProfile
        fields = ('address1', 'birth_date')

        def save(self, commit=True):
            # Save the provided password in hashed format
            user = super(ProfileDetailChangeForm, self).save(commit=False)
            if commit:
                user.save()
            return user

#    def save(self, commit=True):
        # Save the provided password in hashed format
#        user = super(ProfileRegForm, self).save(commit=False)
#        if commit:
#            user.save()
#        return user


#def pre_save_email_activation(sender, instance, *args, **kwargs):
#    if not instance.activated and not instance.forced_expired:
#        if not instance.key:
#            instance.key = unique_key_generator(instance)

#pre_save.connect(pre_save_email_activation, sender=EmailActivation)
