import time

def slow_pow(args: tuple):
    x, y = map(int,args)
    time.sleep(1)
    return x ** y