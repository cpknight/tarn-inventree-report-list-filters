# Tarn InvenTree Report List Filters

An [InvenTree](https://inventree.org/) plugin that adds two template tags for
use in report and label templates:

- **`{% tarn_split %}`** — splits a delimited string into a list you can iterate
- **`{% tarn_replace %}`** — replaces all occurrences of a substring

The tags are registered directly against InvenTree's built-in `report` template
library, so they are available in any template that uses `{% load report %}`.
Both tags can be individually enabled or disabled from the Plugin Settings page
in InvenTree's Admin Center.

All errors are handled gracefully — if something goes wrong the tag returns a
safe default and logs a warning instead of crashing the report.

## Installation

1. Go to **Admin Center → Plugins → Install Plugin**
2. Fill in the form:
   - **Package Name:** `tarn-inventree-report-list-filters`
   - **Source URL:** `git+https://github.com/cpknight/tarn-inventree-report-list-filters.git`
   - **Version:** (leave blank for latest)
3. Check **"Confirm plugin installation"** and click **Install**
4. Enable the plugin in the plugins list
5. Restart InvenTree: `sudo inventree restart`

## Configuration

After enabling the plugin, go to **Admin Center → Plugin Settings → Tarn
Report List Filters**. Two toggle settings are available:

- **Enable tarn_split** (default: on) — controls the `{% tarn_split %}` tag
- **Enable tarn_replace** (default: on) — controls the `{% tarn_replace %}` tag

Disabling a tag causes it to return the original value unchanged.

## Usage

Both tags use Django's `{% simple_tag %}` syntax with the `as` keyword to
assign the result to a template variable. This is the same pattern used by
InvenTree's built-in helpers like `{% getindex %}` and `{% filter_queryset %}`.

### tarn_split

Splits a string by a delimiter and returns a list of trimmed strings.

```
{% load report %}

{% part_parameter part "features" as features %}
{% tarn_split features.data "|" as items %}

<ul>
{% for item in items %}
  <li>{{ item }}</li>
{% endfor %}
</ul>
```

Arguments:
- `value` — the string to split
- `delimiter` — the separator (default `"|"` if omitted)

### tarn_replace

Replaces all occurrences of a substring.

```
{% load report %}

{% tarn_replace part.description "|" ", " as cleaned %}
<p>{{ cleaned }}</p>
```

Arguments:
- `value` — the original string
- `old` — the substring to find
- `new` — the replacement (default `""` if omitted, i.e. deletion)

## How It Works

The plugin registers `tarn_split` and `tarn_replace` as `simple_tag` functions
on InvenTree's `report.templatetags.report` library at import time. This means
no `AppMixin` or custom `templatetags/` directory is needed — the tags appear
automatically when you `{% load report %}`.

This approach follows the recommendation from InvenTree core maintainers
(GitHub issue [#5052](https://github.com/inventree/InvenTree/issues/5052)).

## License

MIT

## Authors

Project Tarn contributors
