import logging

from django.apps import AppConfig

logger = logging.getLogger("inventree")


class TarnReportListFiltersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tarn_inventree_report_list_filters"
    label = "tarn_inventree_report_list_filters"

    def ready(self):
        """Register tarn_split/tarn_replace filters against InvenTree's report library.

        This ensures the filters are available when templates use {% load report %},
        which is InvenTree's standard mechanism for report/label template tags.
        Filters use a 'tarn_' prefix to avoid collisions with Python str methods.
        """
        try:
            from report.templatetags.report import register
            from tarn_inventree_report_list_filters.templatetags.list_filters import (
                tarn_split,
                tarn_replace,
            )

            register.filter("tarn_split", tarn_split)
            register.filter("tarn_replace", tarn_replace)
        except ImportError:
            pass
        except Exception as e:
            logger.warning("Tarn Report List Filters: failed to register filters: %s", e)
