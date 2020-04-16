import memory_profiler

from application import a, b, c


def measured_function(arg):
    print(a(arg))
    print(b(arg))
    print(c(arg))


# Measure the memory usage
mem_usage: list = memory_profiler.memory_usage((measured_function, (5, )))
