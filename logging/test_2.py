import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('log_2')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logging.basicConfig(filename='log_2', level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info("Created Employee: {} {}".format(self.first, self.last))

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


if __name__ == '__main__':
    e1 = Employee('Raman', 'Kutti')
    e1_email = e1.email()

    e2 = Employee('Muhammed', 'Kutti')

    print(e1.first)
    print(e1_email)
