from plugin import InvenTreePlugin
from plugin.mixins import AppMixin, ReportMixin

class ListFiltersPlugin(InvenTreePlugin, AppMixin, ReportMixin):
    NAME = "Report List Filters"
    SLUG = "tarn_report_list_filters"
    TITLE = "Report List Filters"
    DESCRIPTION = "Provides |split and |replace filters for report and label templates"
    VERSION = "1.2.0"
    AUTHOR = "CP Knight"
    AUTHOR_EMAIL = "chris@tarn.parts"
