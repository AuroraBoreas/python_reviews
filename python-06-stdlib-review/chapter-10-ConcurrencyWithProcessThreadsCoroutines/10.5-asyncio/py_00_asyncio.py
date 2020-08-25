"""
! what?
asyncio module provides tools for building concurrent applications using coroutines.
while the `threading` module implements concurrency through application threads, and `multiprocessing`
implements concurrency using system processes.

asyncio uses a single-threaded, single-process approach in which parts of an application
cooperate to switch tasks explicitly at optimal times.

+------------------+-----------------------------------------------------------+-----------------+
| concepts         | explanation                                               | originated from |
+==================+===========================================================+=================+
| threading        | implements concurrency thru application threads           | CPU threads     |
+------------------+-----------------------------------------------------------+-----------------+
| mutliprocessing  | implements concurrency using system processes             | System processes|
+------------------+-----------------------------------------------------------+-----------------+
| asyncio          | use a single-threaded, single-process approach            | see below       |
|                  | in which parts of an application cooperate to switch      |                 |
|                  | tasks explicitly at optimal times.                        |                 |
+------------------+-----------------------------------------------------------+-----------------+




! why?
a chess genius is gonna play with 10 people. one game takes around 3 hours.
the game host wanna terminate these chess games in one day.
what is your solution in this case?

illustration as follows.
            3   
        2       4
    1               5
0        genius         6
                    7
        10      8
            9

            
! how?

asyncio



"""