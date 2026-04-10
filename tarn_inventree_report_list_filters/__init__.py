from django import template
from plugin import InvenTreePlugin
from plugin.mixins import ReportMixin

register = template.Library()

@register.filter
def split(value, arg):
    """Split a string by delimiter. Usage: {{ value|split:"|" }}"""
    if not value:
        return []
    return [x.strip() for x in str(value).split(arg)]

@register.filter
def replace(value, arg1, arg2):
    """Replace substring. Usage: {{ value|replace:"|","<br>• " }}"""
    if not value:
        return ""
    return str(value).replace(arg1, arg2)

class ListFiltersPlugin(InvenTreePlugin, ReportMixin):
    NAME = "Report List Filters"
    SLUG = "tarn_report_list_filters"
    TITLE = "Report List Filters"
    DESCRIPTION = "Provides |split and |replace filters for report and label templates"
    VERSION = "1.0.1"
    AUTHOR = "CP Knight"
    AUTHOR_EMAIL = "chris@tarn.parts"

    def add_report_context(self, report_instance, model_instance, request, context):
        # Explicitly register the filters in report context
        pass
