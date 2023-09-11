'''Hunter Knott, CS 3270, Utah Valley University'''

def track(f):
    cache = {}
    f.count = 0
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cache:
            return cache[key]
        result = f(*args, **kwargs)
        cache[key] = result
        f.count += 1
        wrapper.count = f.count
        print(key + ' found in cache')
        return result
    return wrapper

def log(f):
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a') as logfile:
            logfile.write(f'{f.__name__}{args, kwargs}')
            result = f(*args, **kwargs)
            logfile.write(f'Result: {result}\n')
        return result
    return wrapper

@track
@log
def fib(n):
    return n if n in (0,1) else fib(n-1) + fib(n-2)

def main():
    with open('log.txt', 'w') as logfile:
        logfile.write('')
    print(fib(10), 'calls =', fib.count)

if __name__ == "__main__":
    main()