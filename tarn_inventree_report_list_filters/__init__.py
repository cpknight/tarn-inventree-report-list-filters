from django import template
from InvenTree.plugin import InvenTreePlugin
from plugin.mixins import ReportMixin

register = template.Library()

@register.filter
def split(value, arg):
    """
    Split a string by the given delimiter.
    Example: {{ parameter.data|split:"|" }}
    """
    if not value:
        return []
    return [x.strip() for x in str(value).split(arg)]


@register.filter
def replace(value, arg1, arg2):
    """
    Replace occurrences of arg1 with arg2 in the string.
    Example: {{ parameter.data|replace:"|","<br>• " }}
    """
    if not value:
        return ""
    return str(value).replace(arg1, arg2)


class ListFiltersPlugin(InvenTreePlugin, ReportMixin):
    """
    Provides |split and |replace filters for report and label templates.
    """
    NAME = "TARN Report List Filters"
    SLUG = "tarn_report_list_filters"
    TITLE = "TARN Report List Filters"
    DESCRIPTION = "Adds |split and |replace template filters to make bullet lists from parameters easy"
    VERSION = "1.0.0"
    AUTHOR = "CP Knight"
    AUTHOR_EMAIL = "chris@tarn.parts"

    def add_report_context(self, report_instance, model_instance, request, context):
        """Make the filters available in all reports/labels."""
        pass
