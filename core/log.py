import logging

from core.settings import APP_SETTINGS


logger = logging.Logger(APP_SETTINGS.LOGGER_NAME)

handler = logging.StreamHandler()
handler.setFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def get_logger() -> logging.Logger:
    return logger
