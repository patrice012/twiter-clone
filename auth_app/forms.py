from django import forms
from django.forms import ValidationError
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist


class RegisterForm(forms.ModelForm):
    """
    Create Register form
    """
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget=forms.PasswordInput()

    def clean_email(self):
        data = self.cleaned_data["email"]
        try:
            user = get_user_model().objects.get(email=data)
        except ObjectDoesNotExist:
            return data
        if user:
            raise ValidationError('This email already exist...', code=data)
        
    
