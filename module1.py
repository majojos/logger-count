import logging

logging_A = logging.getLogger('logger_A')
logging_B = logging.getLogger('logger_B')


def run():
    print("hello from %s" % __name__)
    logging_A.warning("warning in '%s'" % __name__)
    logging_A.error("error in '%s'" % __name__)
    logging_A.error("error in '%s'" % __name__)
    logging_A.info("info in '%s'" % __name__)

    logging_B.warning("warning in '%s'" % __name__)
    logging_B.warning("warning in '%s'" % __name__)
