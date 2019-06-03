from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, ListView, DeleteView, TemplateView, CreateView
from django.shortcuts import render, get_object_or_404, redirect

from deal_app.portfolios.forms import PortfolioFrom
from deal_app.portfolios.models import Portfolio


class PortfolioCreateView(CreateView):
    form_class = PortfolioFrom
    template_name = 'portfolios/portfolio_create.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PortfolioCreateView, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super(PortfolioCreateView, self).get_form(form_class)
        form.fields['user'] = self.request.user


portfolio_create_view = PortfolioCreateView.as_view()


class PortfolioListView(LoginRequiredMixin, ListView):
    model = Portfolio


portfolio_list_view = PortfolioListView.as_view()


class PortfolioDetailView(LoginRequiredMixin, DetailView):
    model = Portfolio


portfolio_detail_view = PortfolioDetailView.as_view()


class PortfolioUpdateView(LoginRequiredMixin, UpdateView):
    model = Portfolio
    form_class = PortfolioFrom


portfolio_update_view = PortfolioUpdateView.as_view()


class PortfolioDeleteView(LoginRequiredMixin, DeleteView):
    model = Portfolio
    success_url = reverse_lazy('portfolios:list')


portfolio_delete_view = PortfolioDeleteView.as_view()


def confirm_portfolio_delete_view(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    if request.method == "POST":
        portfolio.delete()
        return redirect('portfolios:detail')
    context = {
        "portfolio": portfolio
    }
    return render(request, "portfolios/portfolio_confirm_delete.html", context)
