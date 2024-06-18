import logging
import allure
from colorama import Fore, Style
import yaml

from data.config_info import ConfigInfo
from data.logs import MsgLog
from src import consts

# handle logger
logger = logging.getLogger("pythonLog")
LOG_COLOR = {
    logging.DEBUG: Fore.CYAN,
    logging.INFO: Fore.GREEN,
    logging.WARNING: Fore.YELLOW,
    logging.ERROR: Fore.RED,
    logging.CRITICAL: Fore.RED + Style.BRIGHT
}


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_color = LOG_COLOR.get(record.levelno, Fore.WHITE)
        message = super().format(record)
        return f"{log_color}{message}{Style.RESET_ALL}"


def record_msg_log(func):
    def wrap(*args):
        msg, *_ = args

        if any(item in str(msg).lower() for item in ("step", "steps", "verify")):
            MsgLog.msg_log.append(msg)

        func(*args)

    return wrap


def setup_logging():
    logger.setLevel(logging.DEBUG)

    # if not logger.hasHandlers():

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = ColoredFormatter('%(asctime)s | %(levelname)s | %(message)s', datefmt="%H:%M:%S")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    _logger = logger.info

    @record_msg_log
    def log_with_record(*args):
        _logger(*args)

    logger.info = log_with_record

    # allure_handler = AllureLogger()
    # allure_handler.setLevel(logging.INFO)
    # logger.addHandler(allure_handler)


def load_config(env):
    logger.info("- Loading confing...")
    path = consts.PROJECT_ROOT / "config" / f"{env}.yaml"

    with open(path, "r") as _config:
        config = yaml.load(_config, Loader=yaml.FullLoader)

        ConfigInfo.url = config["url"]
        ConfigInfo.username = config['username']
        ConfigInfo.password = config["password"]


if __name__ == '__main__':
    setup_logging()
    logger.info("Step 1: hihi")
    logger.info(" hihi ihi")
    logger.info("Verify this is ....")