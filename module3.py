import logging

logging = logging.getLogger('logger_B')


def run():
    print("hello from %s" % __name__)
    logging.warning("warning in '%s'" % __name__)
    logging.error("error in '%s'" % __name__)
    logging.error("error in '%s'" % __name__)
    logging.critical("critical in '%s'" % __name__)
    logging.info("info in '%s'" % __name__)
    logging.info("info in '%s'" % __name__)
