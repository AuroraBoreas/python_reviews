"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

import time
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

def compute(n:int)->list:
    rv = list()
    for i in range(n):
        rv.append(i)
        time.sleep(.5)
    return rv

if __name__ == "__main__":
    logging.info("start..")
    for i in compute(5):
        logging.info(str(i))
    logging.info("end..")