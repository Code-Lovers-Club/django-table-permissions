from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DemoAppConfig(AppConfig):
    name = "demo_app"
    verbose_name = _("Demo application")

    def ready(self):
        super().ready()

        dummy_trans = _("Can deliver pizzas")
        dummy_trans = _("Can do stuff")
        dummy_trans = _("Can do more stuff")
