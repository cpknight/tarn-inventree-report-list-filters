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
    NAME = "TARN Report List Filters"
    SLUG = "tarn_report_list_filters"
    TITLE = "TARN Report List Filters"
    DESCRIPTION = "Adds |split and |replace template filters for reports and labels"
    VERSION = "1.0.0"
    AUTHOR = "CP Knight"
    AUTHOR_EMAIL = "chris@tarn.parts"
