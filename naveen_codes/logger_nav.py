from time import perf_counter

def logger(func):
    def timer(*args, **kwargs):
        print(f"entering {func.__name__}")
        start = perf_counter()
        ret_val = func(*args, **kwargs)
        end = perf_counter()
        print(f"exiting {func.__name__}")
        print(f"total time taken {end-start} seconds")
        return ret_val
    return timer