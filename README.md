# Tarn InvenTree Report List Filters
This plugin adds two template filters for InvenTree reports and labels:

- `|tarn_split:"|"` — splits a delimited string into a list for use with `{% for %}`
- `|tarn_replace:"old,new"` — simple string replacement

Filter names use a `tarn_` prefix to avoid collisions with Python's built-in
`str.split()` and `str.replace()` methods, which can confuse Django's template
resolution. Filters fail gracefully — errors are logged and a safe default is
returned instead of crashing report rendering.

The filters are automatically registered against InvenTree's built-in `report`
template library, so they work alongside all standard report helper functions.

## Usage Example
```
{% load report %}
{% part_parameter part "datasheet_list_features" as features %}

{% for item in features.data|tarn_split:"|" %}
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
