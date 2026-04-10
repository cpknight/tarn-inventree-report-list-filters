from django.apps import AppConfig


class TarnReportListFiltersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tarn_inventree_report_list_filters"
    label = "tarn_inventree_report_list_filters"

    def ready(self):
        """Register split/replace filters against InvenTree's report library.

        This ensures the filters are available when templates use {% load report %},
        which is InvenTree's standard mechanism for report/label template tags.
        """
        try:
            from report.templatetags.report import register
            from tarn_inventree_report_list_filters.templatetags.list_filters import (
                split,
                replace,
            )

            register.filter("split", split)
            register.filter("replace", replace)
        except ImportError:
            pass
