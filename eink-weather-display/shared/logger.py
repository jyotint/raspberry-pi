import os
import yaml
import logging
import logging.config

logConfigurationEnvKey = "eink-weather-display_LOG_CFG"

defaultLogFilePath = "logging.yaml"
defaultLogLevel = logging.INFO
defaultLogStringFormat = "%(asctime)s %(levelname)-8s - %(name)s:%(funcName)s() #  %(message)s"
defaultDateTimeFormat = "%Y-%m-%d %H:%M:%S"


def getLogger(name):
    return logging.getLogger(name)

def setupLogging(
    default_path = defaultLogFilePath,
    default_level = defaultLogLevel,
    env_key = logConfigurationEnvKey):

    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "rt") as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(
            format = defaultLogStringFormat,
            datefmt = defaultDateTimeFormat,
            level = default_level)
