# mos-templates

My [MOS Hub](https://docs.mos-official.net/docs/MOS-Hub/Creating-Your-Own-MOS-Hub-Repository)
repository with plugins and Docker/Compose templates for
[MOS](https://mos-official.net/).

## Contents

### Plugins

| Plugin | Description |
| --- | --- |
| [Tasmota Energy Monitor](plugins/tasmota-energy.json) | Dashboard widget and plugin page showing energy consumption of your Tasmota devices |

### Docker

| Container | Description |
| --- | --- |
| [node-exporter](docker/node-exporter.json) | Prometheus exporter for host hardware and OS metrics |

## Installation

1. Enable the Hub if it is not already: **Settings -> System Configuration -> MOS Hub Settings**.
2. Open **MOS Hub**, click the repositories icon, add this repository and save:

```
https://github.com/jon-rei/mos-templates
```

The plugin appears under **MOS Hub -> Plugins** (category *Home Automation*), the container under **MOS Hub -> Docker**.

## Repository structure

```
├── docker/       # single-container Docker templates
├── compose/      # Docker Compose stack templates (empty for now)
├── plugins/      # system plugins and utilities
├── images/       # icons for templates and plugins
├── maintainer.json
└── README.md
```

## License

[GPL-3.0](LICENSE)
