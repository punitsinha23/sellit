from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter a strong password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Confirm your password'})
    )
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_picture']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter a username'}),
            'email': forms.EmailInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter an email'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password') 
        confirm_password = cleaned_data.get("confirm_password") 

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!") 

        return cleaned_data 


class LoginForm(forms.ModelForm):    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter a strong password'})
    )

    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input input-bordered w-full max-w-xs', 'placeholder': 'Enter an email'}),
        }
