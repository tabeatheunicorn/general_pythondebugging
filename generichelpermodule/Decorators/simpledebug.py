import functools
import time

def decorator(func):
    """Boilerplate decorator code"""
    @functools.wraps(func) # this ensures that the functions metadatat is not messed up.
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

def timer(func):
    """Print the runtime of the decorated function. """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


def call_counter(func):
    """Count how often a function is called."""
    @functools.wraps(func)
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    return helper

## memory profiling:
from memory_profiler import profile
 
 # @profile(precision=?)
 # https://github.com/pythonprofilers/memory_profiler



class Debugger(object):
    import logging

    logger = logging.getLogger(f"{__file__}.Debugger")
    """ Debug a method and return it back"""

    enabled = False

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if self.enabled:
            self.logger.debug(f'Entering : {self.func.__name__}')
            self.logger.debug(f'args, kwargs : {args, kwargs}')
            self.logger.debug(f'{self.func.__name__} returned : {self.func(*args, **kwargs)}')

        return self.func(*args, **kwargs)