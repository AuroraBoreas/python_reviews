"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

from typing import List
import time

def compute(n:int)->List:
    rv = list()
    for i in range(n):
        rv.append(i)
        time.sleep(.5)
    return rv

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info('start..')
    for i in compute(10):
        logging.info(i)
    logging.info('end..')
