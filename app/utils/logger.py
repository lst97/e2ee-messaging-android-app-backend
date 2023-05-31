import logging
from colorama import init, Fore, Style

class Logger:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.DEBUG)
        self.console_handler.setFormatter(logging.Formatter(f"{Fore.CYAN}[%(levelname)s]{Style.RESET_ALL} %(message)s"))
        self.logger.addHandler(self.console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

init()
