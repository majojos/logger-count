import logging


class Callcounted(object):
    """Decorator to determine number of calls for a method"""

    def __init__(self, method):
        self.method = method
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self.method(*args, **kwargs)


class Logger(object):
    # put here levels that should be counted
    logger_levels_to_count = ['warning', 'error', 'critical']

    # put here names of loggers
    logger_names = ['logger_A', 'logger_B', 'logger_C']

    def __init__(self, logfile):
        self._loglevel = logging.INFO
        self._logformat = '%(asctime)s:%(name)s.%(levelname)s:%(message)s'
        self._logfile = logfile
        self._logfilemode = 'w'

        logging.basicConfig(level=self._loglevel, format=self._logformat, filename=self._logfile,
                            filemode=self._logfilemode)

        self.loggers = {}
        self._define_loggers()

    def _define_loggers(self):
        for logger_name in self.logger_names:
            logger = logging.getLogger(logger_name)
            for level_name in self.logger_levels_to_count:
                level = getattr(logger, level_name)
                level = Callcounted(level)
                setattr(logger, level_name, level)
            self.loggers[logger_name] = logger

    def show_summary(self):
        for logger_name in self.logger_names:
            logger = logging.getLogger(logger_name)
            for level_name in self.logger_levels_to_count:
                print("Number of calls for 'logger.level': %s.%s=%s" % (
                    logger_name, level_name, getattr(logger, level_name).counter))
