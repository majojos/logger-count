import sys
from log import Logger
import module1
import module2
import module3


def main():
    loggers = Logger('fe.log')

    # Application code here
    module1.run()
    module2.run()
    module3.run()

    print("test")

    # Logging summary
    print("Logging summary:")
    loggers.show_summary()

if __name__ == '__main__':
    sys.exit(main())
