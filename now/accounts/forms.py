from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from profileacc.models import DocProfile
import pyrebase

User = get_user_model()

config = {

    'apiKey': "AIzaSyB0bEes5zKUjJqiOL7YWtJ0RdtFbhqqDBM",
    'authDomain': "chartsdjango.firebaseapp.com",
    'databaseURL': "https://chartsdjango.firebaseio.com",
    'projectId': "chartsdjango",
    'storageBucket': "chartsdjango.appspot.com",
    'messagingSenderId': "176923102759"
  }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'full_name',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'full_name',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Cannot use this email. It's already registered")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = False #send confirmation email
        if commit:
            user.save()
        return user

#def post_save_user_create_reciever(sender, instance, created, *args, **kwargs):
#    if created:
#        obj = EmailActivation.objects.create(user=instance, email=instance.email)
#        obj.send_activation()

#post_save.connect(post_save_user_create_reciever, sender=User)


class LoginForm(forms.Form):
    email    = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)
#add firebase auth config here
    def clean(self):
        request = self.request
        data = self.cleaned_data
        email  = data.get("email")
        password  = data.get("password")
        #user = auth.sign_in_with_email_and_password(email,password)
        user = auth.sign_in_with_email_and_password(email,password)
        if user is None:
            raise forms.ValidationError("Invalid credentials")
        user = auth.refresh(user['refreshToken'])
        userIdToken = user['idToken']
        # login(request, user)
        self.user = userIdToken
        return data

class UserDetailChangeForm(forms.ModelForm):
    full_name = forms.CharField(label='Name', required=False, widget=forms.TextInput(attrs={"class": 'form-control'}))
    #address1 = forms.CharField(label='Address', required=False, widget=forms.TextInput(attrs={"class": 'form-control'}))

    class Meta:
        model = User
        fields = ['full_name']
