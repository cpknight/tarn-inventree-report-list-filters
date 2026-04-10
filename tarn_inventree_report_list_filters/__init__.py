from plugin import InvenTreePlugin
from plugin.mixins import AppMixin, ReportMixin


class ListFiltersPlugin(InvenTreePlugin, AppMixin, ReportMixin):
    NAME = "Tarn Report List Filters"
    SLUG = "tarn_report_list_filters"
    TITLE = "Tarn Report List Filters"
    DESCRIPTION = "Provides |tarn_split and |tarn_replace filters for report and label templates"
    VERSION = "1.3.0"
    AUTHOR = "CP Knight"
    AUTHOR_EMAIL = "chris@tarn.parts"
