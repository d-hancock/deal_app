from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PropertiesConfig(AppConfig):
    name = "deal_app.properties"
    verbose_name = _("Properties")

    def ready(self):
        try:
            import deal_app.properties.signals  # noqa F401
        except ImportError:
            pass
