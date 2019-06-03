from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import UpdateView, TemplateView, DeleteView, CreateView
from django.utils.decorators import method_decorator

from deal_app.portfolios.models import Portfolio
from deal_app.properties.models import Property, PropertyIncome, PropertyPurchase
from deal_app.properties.forms import PropertyCreateForm, PropertyIncomeForm, PropertyPurchaseForm


class PropertyCreateView(CreateView):
    form_class = PropertyCreateForm
    template_name = 'properties/property_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PropertyCreateView, self).dispatch(*args, **kwargs)

    def get_form(self, form_class=None):
        form = super(PropertyCreateView, self).get_form(form_class)
        form.fields['portfolio'].queryset = Portfolio.objects.filter(user=self.request.user)
        return form


property_create_view = PropertyCreateView.as_view()


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
    form_class = PropertyCreateForm
    template_name = "properties/property_update_form.html"

    def get_success_url(self):
        return reverse('property:detail',
                       kwargs={'pk': self.object.pk})


property_update_view = PropertyUpdateView.as_view()


class PropertyIncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = PropertyIncome
    form_class = PropertyIncomeForm
    template_name = "properties/property_income_update.html"


property_income_update_view = PropertyIncomeUpdateView.as_view()


class PropertyPurchaseUpdateView(LoginRequiredMixin, UpdateView):
    model = PropertyPurchase
    form_class = PropertyPurchaseForm
    template_name = "properties/property_purchase_update.html"

    def get_success_url(self):
        return reverse('property:detail',
                       kwargs={'pk': self.object.pk})


property_purchase_update_view = PropertyPurchaseUpdateView.as_view()
