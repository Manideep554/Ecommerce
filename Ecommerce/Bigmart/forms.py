from .models import *
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
class ProductImageForm(forms.ModelForm):
    class Meta:
        model=ProductImage
        fields='__all__'
class CartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields='__all__'
class UserDetailsForm(forms.Form):
    name=forms.CharField(max_length=20)
    mobile=forms.CharField(max_length=13)
    email=forms.EmailField()
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':22,'rows':4}))
    password=forms.CharField(widget=forms.PasswordInput)
    confirmpassword=forms.CharField(widget=forms.PasswordInput)
