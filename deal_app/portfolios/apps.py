from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PortfoliosConfig(AppConfig):
    name = "deal_app.portfolios"
    verbose_name = _("Portfolios")
