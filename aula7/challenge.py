# Challenge Session 7: Advanced Logging Setup
# Problem: Enhance the logging setup to rotate log files daily and include detailed timestamps.
# Hint: Use TimedRotatingFileHandler from the logging.handlers module.

import logging
from logging.handlers import TimedRotatingFileHandler

def setup_logger():
    logger = logging.getLogger("advanced_logger")
    logger.setLevel(logging.DEBUG)
    handler = TimedRotatingFileHandler(
        "app.log", when="midnight", interval=1, backupCount=7, encoding="utf-8"
    )
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

if __name__ == "__main__":
    logger = setup_logger()
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    print("Logging setup complete. Check app.log for output.")
