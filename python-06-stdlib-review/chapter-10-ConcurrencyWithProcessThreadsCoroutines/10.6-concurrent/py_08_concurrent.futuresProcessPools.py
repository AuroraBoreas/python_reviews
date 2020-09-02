import logging, os
from concurrent import futures

logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(process)d %(message)s')

def futures_process_pool_map():
    def task(n):
        return (n, os.getpid())

    ex = futures.ProcessPoolExecutor(max_workers=2)
    results = ex.map(task, range(5, 0, -1))
    """
    If something happens to one of the worker processes that causes it to exit unexpectedly,
    the ProcessPoolExecutor is considered “broken” and will no longer schedule tasks.
    """
    for n, pid in results:
        logging.debug(f'ran task {n} in process {pid}')

"""
! a big problem here is we can't use "__main__" to run wrapped Process related functions.

! Q: why not?
* A: cuz, just like `multiprocessing` or `asyncio` "Process" obj 
* always has an extra protection on "__main__" to prevent recursive call.

! Q: why can it prevent recursive call?
* A: my guess is "main process" may affect this modules in low level implementation
"""
# if __name__ == "__main__":
#     futures_process_pool_map()

futures_process_pool_map()