import time
import random


def load(*args, **kwargs):
    return {}


def stream_generator(stream_name):

    def counter():
        count = 0
        while True:
            time.sleep(2)
            yield 'data: %s\n\n' % count
            count += 1

    def random_number():
        while True:
            time.sleep(1)
            yield 'data: %s\n\n' % random.random()

    if stream_name == 'counter':
        return counter, 'text/event-stream'
    elif stream_name == 'random-number':
        return random_number, 'text/event-stream'
    else:
        return None, None
