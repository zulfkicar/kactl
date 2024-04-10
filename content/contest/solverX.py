from sys import setrecursionlimit
import threading
import functools
#memoization
@functools.lru_cache(maxsize=none) #add before a func you want to cache
def f():
    return 1
setrecursionlimit(10**6+100)
threading.stack_size(10**6)
t=threading.Thread(target=solve)
t.start()
t.join()