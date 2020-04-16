import memory_profiler

from application import a

@memory_profiler.profile
def profiled_fn():
    a(9)


if __name__ == '__main__':
    profiled_fn()
