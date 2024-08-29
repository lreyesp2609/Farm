    # forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Farmer,Farm,Crop,Livestock,Expense,Sale
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _  # Importar gettext_lazy para traducción

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': _('Username'),
            'email': _('Email'),
            'password1': _('Password'),
            'password2': _('Confirm Password'),
        }

class FarmerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Farmer
        exclude = ['user', 'sales']
        labels = {
            'phone_number': _('Phone Number'),
            'address': _('Address'),
            'city': _('City'),
            'state': _('State'),
            'country': _('Country'),
            'zip_code': _('Zip Code'),
        }

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['farm_name', 'location', 'total_acres', 'description']
        labels = {
            'farm_name': _('Farm Name'),
            'location': _('Location'),
            'total_acres': _('Total Acres'),
            'description': _('Description'),
        }

class CropForm(forms.ModelForm):
    farm = forms.ModelChoiceField(queryset=Farm.objects.all(), empty_label=_("Select a farm"))
    class Meta:
        model = Crop
        fields = ['farm', 'crop_name', 'planting_date', 'harvesting_date', 'yield_amount', 'notes']
        labels = {
            'crop_name': _('Crop Name'),
            'planting_date': _('Planting Date'),
            'harvesting_date': _('Harvesting Date'),
            'yield_amount': _('Yield Amount'),
            'notes': _('Notes'),
        }

class LivestockForm(forms.ModelForm):
    farm = forms.ModelChoiceField(queryset=Farm.objects.all(), empty_label=_("Select a farm"))

    class Meta:
        model = Livestock
        fields = ['farm', 'livestock_type', 'quantity', 'health_status', 'notes']
        labels = {
            'livestock_type': _('Livestock Type'),
            'quantity': _('Quantity'),
            'health_status': _('Health Status'),
            'notes': _('Notes'),
        }

class ExpenseForm(forms.ModelForm):
    farm_name = forms.ModelChoiceField(queryset=Farm.objects.none(), empty_label=None)

    def __init__(self, *args, farmer=None, **kwargs):
        super().__init__(*args, **kwargs)
        if farmer:
            self.fields['farm_name'].queryset = Farm.objects.filter(farmer=farmer)

    class Meta:
        model = Expense
        fields = ['farm_name', 'expense_type', 'expense_date', 'amount', 'description']
        labels = {
            'expense_type': _('Expense Type'),
            'expense_date': _('Expense Date'),
            'amount': _('Amount'),
            'description': _('Description'),
        }

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['budget']
        labels = {
            'budget': _('Budget'),
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product_name', 'quantity', 'unit_price', 'date', 'image', 'farm']
        labels = {
            'product_name': _('Product Name'),
            'quantity': _('Quantity'),
            'unit_price': _('Unit Price'),
            'date': _('Date'),
            'image': _('Image'),
            'farm': _('Farm'),
        }

    def __init__(self, *args, **kwargs):
        farmer = kwargs.pop('farmer', None)
        super().__init__(*args, **kwargs)

        if farmer:
            farms = Farm.objects.filter(farmer=farmer)
            self.fields['farm'].queryset = farms

            has_expense_records = Expense.objects.filter(farmer=farmer).exists()

            if not has_expense_records:
                self.fields['product_name'].widget.attrs['disabled'] = True
                self.fields['quantity'].widget.attrs['disabled'] = True
                self.fields['unit_price'].widget.attrs['disabled'] = True
                self.fields['date'].widget.attrs['disabled'] = True
                self.fields['image'].widget.attrs['disabled'] = True
                self.fields['farm'].widget.attrs['disabled'] = True
                self.fields['farm'].help_text = _('You need to fill in expense details first.')
