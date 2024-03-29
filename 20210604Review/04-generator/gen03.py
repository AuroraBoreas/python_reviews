"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

import time
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def compute(n: int)->int:
    for i in range(n):
        yield i
        time.sleep(.5)

if __name__ == "__main__":
    for i in compute(10):
        logging.debug(repr(i))