import os

from .bot import setup_bot, launch_bot
from .config import load_config
from .db import setup_session_maker
from .logger import setup_logger
from .webhook import setup_app, Application


def webhook_app() -> Application:
    config_path = os.environ.get('CONFIG_PATH', 'config.toml')
    use_env_vars = os.environ.get('CONFIG_USE_ENV_VARS', 'false').lower() in ('1', 'true', 'True', 'TRUE')
    config_env_mapping_path = os.environ.get('CONFIG_ENV_MAPPING_PATH', 'config_env_mapping.toml')
    cfg = load_config(config_path, use_env_vars, config_env_mapping_path)

    bot_logger = setup_logger(cfg.bot.logger)
    db_logger = setup_logger(cfg.db.logger)
    bot_ = setup_bot(bot_config=cfg.bot, logger=bot_logger, db_logger=db_logger)

    app = setup_app(cfg.bot.webhook.path)
    app.ctx.bot = bot_
    app.ctx.secret_token = cfg.bot.webhook.secret_token
    app.ctx.logger = setup_logger(cfg.logger)

    launch_bot(bot_, cfg.bot.drop_pending, True, cfg.bot.allowed_updates, cfg.bot.webhook)
    return app


def main():
    config_path = os.environ.get('CONFIG_PATH', 'config.toml')
    use_env_vars = os.environ.get('CONFIG_USE_ENV_VARS', 'false').lower() in ('1', 'true', 'True', 'TRUE')
    config_env_mapping_path = os.environ.get('CONFIG_ENV_MAPPING_PATH', 'config_env_mapping.toml')

    bot_token = os.environ.get('TOKEN')
    cfg = load_config(config_path, use_env_vars, config_env_mapping_path)
    cfg.bot.token = bot_token
    bot_logger = setup_logger(cfg.bot.logger)

    db_logger = setup_logger(cfg.db.logger)
    db_session_maker = setup_session_maker()

    # TODO: add your extra services here
    # service_name = setup_service(*args)

    bot_ = setup_bot(cfg.bot, db_session_maker, db_logger, bot_logger)

    launch_bot(bot_, cfg.bot.drop_pending, False, cfg.bot.allowed_updates, cfg.bot.webhook)


if __name__ == "__main__":
    main()
