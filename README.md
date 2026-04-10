# :mountain: Tarn InvenTree Report List Filters

An [InvenTree](https://inventree.org/) plugin that adds two template tags for
use in report and label templates:

| Tag | What it does |
|---|---|
| **`{% tarn_split %}`** | Splits a delimited string into a list you can iterate with `{% for %}` |
| **`{% tarn_replace %}`** | Replaces all occurrences of a substring |

:white_check_mark: Tags are available via `{% load report %}` — no extra `{% load %}` needed
:gear: Each tag can be toggled on/off from **Plugin Settings** in the Admin Center
:shield: Errors are handled gracefully — safe defaults are returned instead of crashing reports

---

## :package: Installation

1. Go to **Admin Center → Plugins → Install Plugin**
2. Fill in the form:
   - **Package Name:** `tarn-inventree-report-list-filters`
   - **Source URL:** `git+https://github.com/cpknight/tarn-inventree-report-list-filters.git`
   - **Version:** (leave blank for latest)
3. Check **"Confirm plugin installation"** and click **Install**
4. Enable the plugin in the plugins list
5. Restart InvenTree: `sudo inventree restart`

---

## :gear: Configuration

After enabling the plugin, go to **Admin Center → Plugin Settings → Tarn
Report List Filters**. Two toggle settings are available:

| Setting | Default | Effect when disabled |
|---|---|---|
| **Enable tarn_split** | :white_check_mark: On | Returns the original value as a single-element list |
| **Enable tarn_replace** | :white_check_mark: On | Returns the original value unchanged |

---

## :memo: Usage

Both tags use Django's `{% simple_tag %}` syntax with the `as` keyword to
assign the result to a template variable. This is the same pattern used by
InvenTree's built-in helpers like `{% getindex %}` and `{% filter_queryset %}`.

### :scissors: tarn_split

Splits a string by a delimiter and returns a list of trimmed strings.

```html
{% load report %}

{% part_parameter part "features" as features %}
{% tarn_split features.data "|" as items %}

<ul>
{% for item in items %}
  <li>{{ item }}</li>
{% endfor %}
</ul>
```

| Argument | Description | Default |
|---|---|---|
| `value` | The string to split | *(required)* |
| `delimiter` | The separator character(s) | `"|"` |

### :arrows_counterclockwise: tarn_replace

Replaces all occurrences of a substring.

```html
{% load report %}

{% tarn_replace part.description "|" ", " as cleaned %}
<p>{{ cleaned }}</p>
```

| Argument | Description | Default |
|---|---|---|
| `value` | The original string | *(required)* |
| `old` | The substring to find | *(required)* |
| `new` | The replacement string | `""` (deletion) |

---

## :wrench: How It Works

The plugin registers `tarn_split` and `tarn_replace` as `simple_tag` functions
on InvenTree's `report.templatetags.report` library at import time. This means
no `AppMixin` or custom `templatetags/` directory is needed — the tags appear
automatically when you `{% load report %}`.

This approach follows the recommendation from InvenTree core maintainers
(GitHub issue [#5052](https://github.com/inventree/InvenTree/issues/5052)).

---

## :page_facing_up: License

MIT

---

## :busts_in_silhouette: Authors

[Project Tarn](https://tarn.parts) contributors, with development assistance
from [Oz](https://warp.dev) (Warp AI).

### About Project Tarn

[The Tarn Project](https://tarn.parts) is developing the **Tarn Production
System (TPS)** — a modular microfactory designed to make small-scale
manufacturing more practical and less dependent on large centralised facilities
and long supply chains. TPS is built so that a single operator can manage
meaningful production volumes, from design through to packaging, without
requiring massive capital or dedicated buildings. The system is built around
self-hosted management and control (including InvenTree) that keeps inventory,
scheduling, quality records, and critical data under local control.
