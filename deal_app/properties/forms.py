from django import forms
from django.utils.translation import ugettext_lazy as _
from deal_app.properties.models import PropertyIncome, Property, PropertyPurchase
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class PropertyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['portfolio']
        labels = {
            'street_address': _(''),
            'city': _(''),
            'zip_code': _(''),
            'state': _(''),
            'number_units': _(''),
            'estimated_value': _(''),
            'last_price': _(''),
            'mls_number': _(''),
            'prop_tax': _(''),
            'bedrooms': _(''),
            'prop_type': _('Type of property'),
        }


class PropertyIncomeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropertyIncomeForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        class Meta:
            model = PropertyIncome
            fields = '__all__'
            exclude = ['property']
            labels = {
                'gross_monthly_rent': _('Gross Monthly Rent'),
                'electricity': _('Electricity'),
                'water_sewer': _('Water & Sewer'),
                'pmi': _('PMI'),
                'garbage': _('Garbage'),
                'hoas': _('HOAs'),
                'monthly_insurance': _('Monthly Insurance'),
                'vacancy_percent': _('Vacancy (%)'),
                'maintenance': _('Maintenance (%)'),
                'capex': _('Capital Expenditures (%)'),
                'management_fees_percent': _('Management Fees (%)'),
                'annual_income_growth': _('Annual Income Growth (%)'),
                'annual_appreciation': _('Annual Appreciation(%)'),
                'annual_expense_growth': _('Annual Expense Growth (%)')
            }


class PropertyPurchaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropertyPurchaseForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        class Meta:
            model = PropertyPurchase
            fields = '__all__'
            exclude = ['property']
            labels = {
                'purchase_price': _('Purchase Price'),
                'after_repair_value': _('Value After Repairs'),
                'closing_cost_general': _('Closing Costs'),
                'estimated_repair_general': _('Repairs Cost'),
                'cash_deal': _('Is This A Cash Deal?'),
                'down_payment_percent': _('% Down Payment'),
                'loan_interest_rate': _('Loan interest rate'),
                'lender_points': _('Lender Points'),
                'misc_lender_charges': _('MISC Loan Charges'),
                'years_amortized': _('Loan Term Length'),
            }
