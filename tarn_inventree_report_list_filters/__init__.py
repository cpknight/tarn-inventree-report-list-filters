"""Tarn Report List Filters - InvenTree plugin.

Provides {% tarn_split %} and {% tarn_replace %} template tags for report
and label templates. Tags are registered directly against InvenTree's
built-in 'report' template library so they are available via {% load report %}.

This follows the approach recommended by InvenTree core maintainers:
  "import the library register of any templatetag and register your tags
   against that, in either the init() or the plugin class."
  -- matmair, InvenTree GitHub issue #5052
"""

import logging

from plugin import InvenTreePlugin
from plugin.mixins import ReportMixin, SettingsMixin

logger = logging.getLogger("inventree")

# ---------------------------------------------------------------------------
# Register template tags against InvenTree's report library at import time.
# ---------------------------------------------------------------------------
try:
    from report.templatetags.report import register

    @register.simple_tag()
    def tarn_split(value, delimiter="|"):
        """Split a string by a delimiter, returning a list of stripped strings.

        Usage in a report or label template:
            {% load report %}
            {% tarn_split my_variable "|" as items %}
            {% for item in items %}
                {{ item }}
            {% endfor %}
        """
        try:
            from plugin.registry import registry

            plugin = registry.get_plugin("tarn_report_list_filters")
            if plugin and not plugin.get_setting("ENABLE_SPLIT"):
                return [str(value)] if value else []
        except Exception:
            pass

        try:
            if not value:
                return []
            return [x.strip() for x in str(value).split(str(delimiter))]
        except Exception as e:
            logger.warning("tarn_split error: %s", e)
            return []

    @register.simple_tag()
    def tarn_replace(value, old, new=""):
        """Replace all occurrences of a substring.

        Usage in a report or label template:
            {% load report %}
            {% tarn_replace my_variable "|" ", " as result %}
            {{ result }}
        """
        try:
            from plugin.registry import registry

            plugin = registry.get_plugin("tarn_report_list_filters")
            if plugin and not plugin.get_setting("ENABLE_REPLACE"):
                return str(value) if value else ""
        except Exception:
            pass

        try:
            if not value:
                return ""
            return str(value).replace(str(old), str(new))
        except Exception as e:
            logger.warning("tarn_replace error: %s", e)
            return str(value) if value else ""

except ImportError:
    logger.info(
        "Tarn Report List Filters: report.templatetags.report not available; "
        "template tags will not be registered."
    )
except Exception as e:
    logger.warning(
        "Tarn Report List Filters: failed to register template tags: %s", e
    )


# ---------------------------------------------------------------------------
# Plugin class
# ---------------------------------------------------------------------------
class TarnReportListFiltersPlugin(SettingsMixin, ReportMixin, InvenTreePlugin):
    """Provides tarn_split and tarn_replace template tags for reports/labels."""

    NAME = "Tarn Report List Filters"
    SLUG = "tarn_report_list_filters"
    TITLE = "Tarn Report List Filters"
    DESCRIPTION = (
        "Adds {% tarn_split %} and {% tarn_replace %} template tags "
        "for InvenTree report and label templates."
    )
    VERSION = "1.3.1"
    AUTHOR = "Project Tarn contributors"
    WEBSITE = "https://github.com/cpknight/tarn-inventree-report-list-filters"

    SETTINGS = {
        "ENABLE_SPLIT": {
            "name": "Enable tarn_split",
            "description": (
                "Enable the {% tarn_split %} template tag "
                "for reports and labels"
            ),
            "validator": bool,
            "default": True,
        },
        "ENABLE_REPLACE": {
            "name": "Enable tarn_replace",
            "description": (
                "Enable the {% tarn_replace %} template tag "
                "for reports and labels"
            ),
            "validator": bool,
            "default": True,
        },
    }
