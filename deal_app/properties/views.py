from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView, ListView, TemplateView, DeleteView, CreateView

from deal_app.properties.models import Property, PropertyIncome, PropertyPurchase
from deal_app.properties.forms import PropertyForm, PropertyIncomeForm, PropertyPurchaseForm


class PropertyListView(LoginRequiredMixin, TemplateView):
    template_name = "properties/property_list.html"


property_list_view = PropertyListView.as_view()


class PropertyDetailView(LoginRequiredMixin, TemplateView):
    template_name = "properties/property_detail.html"


property_detail_view = PropertyDetailView.as_view()


class PropertyDeleteView(LoginRequiredMixin, DeleteView):
    model = DeleteView


property_delete_view = PropertyDeleteView.as_view()


class PropertyUpdateView(LoginRequiredMixin, UpdateView):
    model = Property
    form_class = PropertyForm

    def get_success_url(self):
        return reverse('property:detail',
                       kwargs={'pk': self.object.pk})


property_update_view = PropertyUpdateView.as_view()


class PropertyIncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = PropertyIncome
    form_class = PropertyIncomeForm
    template_name = 'properties/property_income_update.html'

    def get_success_url(self):
        return reverse('property:detail',
                       kwargs={'pk': self.object.pk})


property_income_update_view = PropertyUpdateView.as_view()


class PropertyPurchaseUpdateView(LoginRequiredMixin, UpdateView):
    model = PropertyPurchase
    form_class = PropertyPurchaseForm
    template_name = 'properties/property_purchase_update.html'

    def get_success_url(self):
        return reverse('property:detail',
                       kwargs={'pk': self.object.pk})


property_purchase_update_view = PropertyUpdateView.as_view()
