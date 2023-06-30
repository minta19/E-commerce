from django import forms
from django.contrib.auth import get_user_model
from ProductApp.models import Product
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()

class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class AddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['P_name', 'Price', 'Quantity', 'image']

class EditProductQuantityForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Quantity']
        widgets = {
            'Quantity': forms.NumberInput(attrs={'class': 'form-control'})
        }
        