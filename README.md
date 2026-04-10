# Tarn InvenTree Report List Filters
This plugin adds two very useful template filters for InvenTree reports and labels:

- `|split:"|"` — splits a pipe-separated parameter value into a list so you can loop with `{% for %}`
- `|replace:"old,new"` — simple string replacement

The filters are automatically registered against InvenTree's built-in `report`
template library, so they work alongside all standard report helper functions.

## Usage Example
```
{% load report %}
{% part_parameter part "datasheet_list_features" as features %}

{% for item in features.data|split:"|" %}
  {{ item }}
{% endfor %}
```

## Installation via Admin Center

- Go to Admin Center → Plugins → Install Plugin
- Fill in the form as follows:
  - Package Name: `tarn-inventree-report-list-filters`
  - Source URL: `git+https://github.com/cpknight/tarn-inventree-report-list-filters.git`
  - Version: (leave blank)
- Check `"Confirm plugin installation"`, Click `Install`
- After installation, enable the plugin in the plugins list
- Restart InvenTree with: `sudo inventree restart`
