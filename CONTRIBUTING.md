# Template guidelines

Conventions for templates in this repository. Follow them when adding or changing a template.

See the [MOS Hub repository docs](https://docs.mos-official.net/docs/MOS-Hub/Creating-Your-Own-MOS-Hub-Repository)
for the general format.

## Setup

The repository uses [pre-commit](https://pre-commit.com). Install it once (e.g. `uv tool install pre-commit`
or `pipx install pre-commit`), then enable the hooks once per clone:

```sh
pre-commit install
```

On every commit the hooks validate JSON/YAML, fix trailing whitespace and final newlines, and
run `scripts/format-templates.py` on Docker templates. If a hook changes files, the commit is aborted.
Review the changes, stage them, and commit again. To run all hooks manually: `pre-commit run --all-files`.

## Checklist for a new template

1. Add the template file (`docker/<name>.json`, `compose/<name>/` or `plugins/<name>.json`).
2. For Docker templates, run `scripts/format-templates.py` to apply the key order and formatting
   (the pre-commit hook does this too).
3. Add a row to the matching table in [README.md](README.md).
4. Test the template in MOS before pushing.

## Docker templates (`docker/`)

### Key order

Keys are grouped by purpose. `scripts/format-templates.py` enforces this order, and
`scripts/format-templates.py --check` reports files that don't follow it.

| Group | Keys |
| --- | --- |
| What it is | `name`, `description`, `category`, `icon` |
| Links | `project`, `readme_url`, `support` |
| Image | `repo`, `registry`, `architecture` |
| Runtime | `network`, `custom_ip`, `privileged`, `default_shell`, `no_autoupdate`, `extra_parameters`, `post_parameters`, `web_ui_url` |
| Mappings | `paths`, `ports`, `variables`, `devices`, `labels` |

Formatting: 2-space indent, and lists of plain values on one line (`[ "amd64", "arm64" ]`).
Leave out `gpus` unless the container needs a GPU.

### Content

- **`name`**: the lowercase upstream project name, e.g. `node-exporter`.
- **`description`**: what the container does, the URL it serves (e.g. `http://<ip>:9100/metrics`), and any
  setup the user has to do after deploying (config files to edit, parameters to adjust).
- **`category`**: only values from the MOS category list (case sensitive): AI, Backup, Crypto, Downloader,
  Driver, Game Server, Home Automation, Hosting, Media, Monitoring, Network, Productivity, Security,
  System, Utilities, Misc.
- **`icon`**: prefer [homarr dashboard-icons](https://github.com/homarr-labs/dashboard-icons) via
  `https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/png/<name>.png`. If no icon exists there, add
  a 256x256 PNG to `images/` and reference it through `https://raw.githubusercontent.com/jon-rei/mos-templates/main/images/<name>.png`.
- **`support`**: the upstream project's issue tracker, not this repository.
- **`architecture`**: only the architectures the image is actually published for.

### Runtime

- **Restart policy**: always include `--restart=unless-stopped` in `extra_parameters`.
- **User**: containers run as `500:500`, the MOS default.
  - If the image supports `PUID`/`PGID`, add them as variables with value `500`.
  - Otherwise add `--user=500:500` to `extra_parameters`.
- **Docker flags** (`--pid`, `--cap-add`, `--user`, ...) go into `extra_parameters`; arguments for the
  container's own command go into `post_parameters`.
- **Appdata**: persistent data is mounted from `/mnt/cache/appdata/<name>`.
- **Ports**: keep the upstream default port, with the same port on host and container.
- **Variables**: name them `<Label>: <KEY>`, e.g. `Router Password: DRAYTEK_PASSWORD`. Mark secrets with
  `"mask": true`, and mark values the container can't start without with `"required": true`.

## Compose templates (`compose/<name>/`)

- Each stack folder contains `compose.yaml` and `template.json`, plus an optional `.env` for values users
  should change (port, timezone, appdata path).
- The same runtime rules apply: `restart: unless-stopped`, `500:500` for services that write to appdata,
  and `/mnt/cache/appdata/<name>` for persistent data.

## Plugins (`plugins/`)

- The required keys are `name`, `description`, `category`, `repository` and `architecture`.
- `support` points to the plugin repository's issue tracker.
