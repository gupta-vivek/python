import logging


logging.basicConfig(filename='log_1', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


num1 = 10
num2 = 5

a = add(num1, num2)
logging.debug("Add: {} + {} = {}".format(num1, num2, a))

s = subtract(num1, num2)
logging.debug("Subtract: {} - {} = {}".format(num1, num2, s))
