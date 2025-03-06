from django import forms
from django.contrib.auth.models import User
from .models import Profile

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

class ProfileUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label="Username")
    profile_picture = forms.ImageField(required=False, label="Profile Picture")  

    class Meta:
        model = Profile
        fields = ["profile_picture"]  # Profile picture is part of Profile model

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username  # Pre-fill username

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user

        # Update username if changed
        new_username = self.cleaned_data.get("username")
        if new_username and user.username != new_username:
            user.username = new_username
            user.save()

        if commit:
            profile.save()

        return profile