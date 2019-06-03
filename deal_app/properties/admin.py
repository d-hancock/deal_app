from django.contrib import admin

from deal_app.properties.models import Property, PropertyPurchase, PropertyIncome

admin.site.register(Property)
admin.site.register(PropertyPurchase)
admin.site.register(PropertyIncome)
