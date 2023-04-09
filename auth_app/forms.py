from django import forms

from django.contrib.auth import get_user_model


class RegisterForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget=forms.PasswordInput()

    def clean_email(self):
        data = self.cleaned_data["email"]
        user = get_user_model().objects.get(email=data)
        if user:
            raise ValidationError('This email already exist...', code=data)
        return data
    