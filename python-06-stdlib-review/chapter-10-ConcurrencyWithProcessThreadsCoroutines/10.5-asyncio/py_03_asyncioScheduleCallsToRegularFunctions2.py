"""
Table: difference between asyncio.get_event_loop.call_soon() and asyncio.get_event_loop.call_later()

+---------------+----------------+---------------+
| diff          | call_soon()    | call_later()  |
+---------------+----------------+---------------+


"""


import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(asctime)s) %(message)s',
)

def asyncio_call_later():
    def callback(n):
        logging.debug(f'callback {n} invoked')

    async def main_job(loop):
        logging.debug('register callbacks')
        loop.call_later(0.2, callback, 1)
        loop.call_later(0.1, callback, 2)
        loop.call_soon(callback, 3)
        await asyncio.sleep(.4)

    event_loop = asyncio.get_event_loop()
    try:
        logging.debug('entering event loop')
        event_loop.run_until_complete(main_job(event_loop))
    finally:
        logging.debug('exiting event loop')
        event_loop.close()

if __name__ == "__main__":
    asyncio_call_later()