import time

def slow_pow(args: tuple)->int:
    x, y = map(int,args)
    time.sleep(1)
    return x ** y


def slow_add(args: tuple)->int:
    x, y = map(int,args)
    time.sleep(1)
    return x + y
