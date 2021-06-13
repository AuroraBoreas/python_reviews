"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

import time
import logging
logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(message)s')

def compute(n: int)->int:
    for i in range(n):
        yield i
        time.sleep(.5)

if __name__ == "__main__":
    logging.warning('start..')
    for i in compute(5):
        logging.warning(str(i))
    logging.warning('end..')