# TARN InvenTree Report List Filters

This plugin adds two very useful template filters for InvenTree reports and labels:

- `|split:"|"` — splits a pipe-separated parameter value into a list so you can loop with `{% for %}`
- `|replace:"old","new"` — simple string replacement

### Usage Example

```django
{% part_parameter part "datasheet_list_features" as features %}

<ul>
{% for item in features.data|split:"|" %}
  <li>{{ item }}</li>
{% endfor %}
</ul>
```
