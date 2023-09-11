from timeit import default_timer as timer
import time as _time

def timedec(f):
    if not hasattr(timedec, 'times'):
        timedec.times = []
    def wrapper(*args):
        start_time = timer()
        result = f(*args)
        end_time = timer()
        ex_time = end_time - start_time
        timedec.times.append(ex_time)
        return result
    wrapper.times = timedec.times
    return wrapper

def main():
    # Same as 'fun1 = timedec(fun1)'
    @timedec
    def fun1(seconds):
        _time.sleep(seconds)

    for t in [.1, .2, .3, .4, .5, .6, .7, .8, .9]:
        fun1(t)
    print(fun1.times)
    print(", ".join(['{:.2f}'.format(t) for t in fun1.times]))

if __name__ == "__main__":
    main()
