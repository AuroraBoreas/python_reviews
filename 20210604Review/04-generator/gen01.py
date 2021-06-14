"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

import time

def compute(n: int)->list:
    rv = list()
    for i in range(n):
        rv.append(i)
        time.sleep(.5)
    return rv

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
    for i in compute(10):
        logging.debug(repr(i))