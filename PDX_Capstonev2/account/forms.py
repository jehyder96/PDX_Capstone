from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

    #function to validate responses
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            #raise a validation error
            raise forms.validationError('This email is invalid')
        
        if len(email) >= 200:
            raise forms.ValidationError('Your email is too long')
        #must add return email or it won't get saved
        return email