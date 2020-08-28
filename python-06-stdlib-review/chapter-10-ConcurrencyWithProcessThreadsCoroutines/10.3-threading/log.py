import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(message)-10s',
)

def log_daemon():
    a = range(10)
    b = list('abcdefghij')
    import itertools
    for i, j in itertools.zip_longest(a, b):
        logging.debug('%s * %s = %s', j, i, repr(j * i))
    
    pass


if __name__ == "__main__":
    log_daemon()