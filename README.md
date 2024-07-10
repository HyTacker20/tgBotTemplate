# tgBotTemplate

Simple, but extensible template for telegram bot,
using [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI), 
[adaptix](https://github.com/reagento/dataclass-factory/tree/3.x/develop),
[SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)
and [alembic](https://github.com/sqlalchemy/alembic)

## Installation

```bash
git clone https://github.com/HyTacker20/tgBotTemplate  # via HTTPS
# or
git clone git@github.com:HyTacker20/tgBotTemplate.git  # via SSH

cd tgBotTemplate
```

- Change package name, description, version, author, homepage, etc. in `pyproject.toml`
- Create [virtual environment](https://pipenv.pypa.io/en/latest/installation.html) or use the
  existing one
- Activate virtual environment 
- Install the package in editable mode

```bash
pip install -e src/.
```

## Usage

Before running the bot you'll have to configure the environment
using the environment variables

| Environment variable    | Description                                                 | Allowed values                    |
|-------------------------|-------------------------------------------------------------|-----------------------------------|
| CONFIG_PATH             | Path to the config file to use                              | Default `config.toml`             |
| CONFIG_USE_ENV_VARS     | Override config file with environment variables             | `True`, `1`<br/>Default `False`   |
| CONFIG_ENV_MAPPING_PATH | Path to the file with mapping of config values and env vars | Default `config_env_mapping.toml` |

To run the bot using long polling use the script

```bash
python -m src.mypackage
```

To run the bot using webhook, you'll have to adjust the module `mypackage:webhook`
according to the web-framework used

After that, you can launch the app using the web-server of your choice, e.g. `gunicorn`

```bash
gunicorn 'mypackage:webhook_app()' --bind=$HOST:$PORT --workers-class=$WORKERS_CLASS
```

## Uninstall

```bash
pip uninstall <your-package-title>
```

Beware that `mypackage` is not the package name, but the name of the module,
the package name is defined in `pyproject.toml`

## Author

This project is a fork of the original repository [Cub11k/tgBotTemplate](https://github.com/Cub11k/tgBotTemplate).

