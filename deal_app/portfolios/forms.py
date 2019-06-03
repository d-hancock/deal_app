from django import forms
from django.utils.translation import ugettext_lazy as _
from deal_app.portfolios.models import Portfolio
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class PortfolioFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PortfolioFrom, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

    class Meta:
        model = Portfolio
        fields = ('name', 'unit_cashflow_criteria')
        exclude = ['user']
        labels = {
            'name': _('Portfolio Name'),
            'unit_cashflow_criteria': _('Per unit cash flow criteria')
        }
