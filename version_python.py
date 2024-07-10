import time

def fibonacci(n):
    if n<=1:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_caching(n, cacher=None):
    if cache is None:
        cache= ()
        if n<=1:
            return n
        if n in cache:
            return cache(n)
        result = fibonacci_caching(n-1, cache)+ fibonacci_caching(n-2, cache)
        return result


def main():
    print("programacion dinamica")

    star_time = time.time_ns()
    print(fibonacci(4))
    end_time =time.time_ns()
    print(f"Time taken: (end_time-star_time) ns")

    star_time = time.ns()
    print(fibonacci_caching(4))
    end_time =time.time_ns()
    print(f"time token: {end_time-star_time} ns")
