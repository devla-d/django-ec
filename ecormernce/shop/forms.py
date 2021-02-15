from django import forms 
from .models import Shipping


class CheckOutForm(forms.ModelForm):

    class Meta:
        model = Shipping
        fields = ['Address','phone_no','zip_code','city','state','country','billing_address','shipping_address']