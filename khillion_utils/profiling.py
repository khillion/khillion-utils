import cProfile
import functools


def profile(file_path):
    def decorator_profile(func):
        @functools.wraps(func)
        def wrapper_profile(*args, **kwargs):
            cp = cProfile.Profile()
            cp.enable()
            value = func(*args, **kwargs)
            cp.disable()
            cp.dump_stats(file_path)
            return value

        return wrapper_profile

    return decorator_profile

