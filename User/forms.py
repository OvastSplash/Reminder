from django import forms
from .models import User
from django.contrib.auth import authenticate

class UserLoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your username'
        })
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your password'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password")
        
        return cleaned_data
    

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_name(self):
        username = self.cleaned_data.get('username')

        if username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError("A user with that username already exists")
            return username            

        raise forms.ValidationError("Username cannot be empty")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match")

            return cleaned_data    

        raise forms.ValidationError("Password fields cannot be empty")

    def save(self, commit=True):
        password = self.cleaned_data.get("password")
        user = super().save(commit=False)
        user.set_password(password)
        
        if commit:
            user.save()
        return user