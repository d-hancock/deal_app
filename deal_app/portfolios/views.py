from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, ListView, DeleteView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from deal_app.portfolios.forms import PortfolioFrom

from .models import Portfolio


class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = Portfolio
    form_class = PortfolioFrom


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
    return render(request,"portfolios/portfolio_confirm_delete.html", context)
