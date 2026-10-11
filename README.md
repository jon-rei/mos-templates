# mos-templates

My [MOS Hub](https://docs.mos-official.net/docs/MOS-Hub/Creating-Your-Own-MOS-Hub-Repository)
repository with plugins and Docker/Compose templates for
[MOS](https://mos-official.net/).

## Contents

### Plugins

| Plugin | Description |
| --- | --- |
| [Tasmota Energy Monitor](plugins/tasmota-energy.json) | Dashboard widget and plugin page showing energy consumption of your Tasmota devices |

## Installation

Add this repository to your MOS instance:

**Settings -> System Configuration -> MOS Hub Settings -> MOS Hub**

```
https://github.com/jon-rei/mos-templates
```

Click **Refresh**, then browse **Docker -> MOS Hub** — the plugin appears under
**Home Automation**.

The Tasmota Energy Monitor is installed from
[jon-rei/mos-tasmota](https://github.com/jon-rei/mos-tasmota); see its
[README](https://github.com/jon-rei/mos-tasmota/blob/main/README.md) for
configuration (devices, refresh interval, electricity price).

## Repository structure

```
├── docker/       # single-container Docker templates (empty for now)
├── compose/      # Docker Compose stack templates (empty for now)
├── plugins/      # system plugins and utilities
├── images/       # icons for templates and plugins
├── maintainer.json
└── README.md
```

## License

[GPL-3.0](LICENSE)
