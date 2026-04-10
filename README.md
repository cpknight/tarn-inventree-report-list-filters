# Tarn InvenTree Report List Filters
This plugin adds two very useful template filters for InvenTree reports and labels:

- `|split:"|"` — splits a pipe-separated parameter value into a list so you can loop with {% for %}
- `|replace:"old","new"` — simple string replacement

## Usage Example
```
{% part_parameter part "datasheet_list_features" as features %}

{% for item in features.data|split:"|" %}
  {{ item }}
{% endfor %}
```

## Installation

- Go to `Admin Center` → `Plugins` → `Install Plugin`
- Enter this GitHub URL: `https://github.com/cpknight/tarn-inventree-report-list-filters`
- Install and enable the plugin
- Restart InvenTree (`sudo inventree restart`)

Now you can create clean bullet lists from pipe-separated parameters.
