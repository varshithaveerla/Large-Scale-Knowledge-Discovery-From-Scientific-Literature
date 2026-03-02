"""
performance_profiler.py

Utility script for profiling runtime and scalability behavior of the pipeline.
"""

import time

def profile_execution(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"Execution time: {end - start:.2f} seconds")
    return result
