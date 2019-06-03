from django.db import models
from django.urls import reverse
from deal_app.portfolios.models import Portfolio

"""
Base Property model 
"""


class Property(models.Model):
    portfolio = models.ForeignKey("portfolios.Portfolio", on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    state = models.CharField(max_length=20)
    number_units = models.IntegerField(blank=True, null=True)
    estimated_value = models.FloatField(blank=True, null=True)
    last_price = models.FloatField(blank=True, null=True)
    mls_number = models.CharField(max_length=100, blank=True, null=True)
    prop_tax = models.FloatField(blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    single_family_home = 'SFH'
    duplex = 'DUP'
    triplex = 'TRP'
    fourplex = 'FRP'
    mulifamily = 'MF'
    prop_type_choices = [
        (single_family_home, 'Single Family Home'),
        (duplex, 'Duplex'),
        (triplex, 'Triplex'),
        (fourplex, 'Fourplex'),
        (mulifamily, 'Multi-Family')
    ]
    prop_type = models.CharField(
        max_length=3,
        choices=prop_type_choices,
        default=single_family_home
    )

    class Meta:
        verbose_name_plural = "Properties"


"""
Unit detail model holding all related per unit information associated with property.
"""


class Unit(models.Model):
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE)
    number_bedrooms = models.IntegerField()
    number_bathrooms = models.IntegerField()
    total_sq_foot = models.IntegerField()
    year_built = models.IntegerField()
    unit_rent = models.FloatField()


"""
Property Purchase Model. Deals with information regarding the intial purchase of a property.        
"""


class PropertyPurchase(models.Model):
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE)
    purchase_price = models.FloatField()
    after_repair_value = models.FloatField(default=purchase_price)
    closing_cost_general = models.FloatField(blank=True, null=True)
    estimated_repair_general = models.FloatField(blank=True, null=True)
    cash_deal = models.BooleanField(default=False)
    down_payment_percent = models.FloatField(blank=True, null=True)
    loan_interest_rate = models.FloatField(blank=True, null=True)
    lender_points = models.FloatField(blank=True, null=True)
    misc_lender_charges = models.FloatField(blank=True, null=True)
    years_amortized = models.FloatField()


"""
Property monthly finances model tracking income and expenses for associated property. 
"""


class PropertyIncome(models.Model):
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE)
    gross_monthly_rent = models.FloatField(blank=True, null=True)
    electricity = models.FloatField(blank=True, null=True)
    water_sewer = models.FloatField(blank=True, null=True)
    pmi = models.FloatField(blank=True, null=True)
    garbage = models.FloatField(blank=True, null=True)
    hoas = models.FloatField(blank=True, null=True)
    monthly_insurance = models.FloatField(blank=True, null=True)
    vacancy_percent = models.FloatField(blank=True, null=True)
    maintenance = models.FloatField(blank=True, null=True)
    capex = models.FloatField(blank=True, null=True)
    management_fees_percent = models.FloatField(blank=True, null=True)
    annual_income_growth = models.FloatField(blank=True, null=True)
    annual_appreciation = models.FloatField(blank=True, null=True)
    annual_expense_growth = models.FloatField(blank=True, null=True)
