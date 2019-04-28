from contextlib import contextmanager
import time


@contextmanager
def time_it():
    start = time.time()
    yield
    end = time.time()
    print(f"ellspad: {end - start}")


if __name__ == '__main__':
    with time_it():
        var = (x for x in range(100000000))
