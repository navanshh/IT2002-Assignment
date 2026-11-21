# Navansh Mandowara - 25BEC066
# Lab 2: Prefix Averages (Quadratic vs Linear Time)

import time
import math
import random


def prefix_average1(sequence):
    length = len(sequence)
    averages = [0.0] * length
    for i in range(length):
        prefix_sum = 0.0
        for j in range(i + 1):
            prefix_sum += sequence[j]
        averages[i] = prefix_sum / (i + 1)
    return averages


def prefix_average2(sequence):
    length = len(sequence)
    averages = [0.0] * length
    accumulator = 0.0
    for i in range(length):
        accumulator += sequence[i]
        averages[i] = accumulator / (i + 1)
    return averages


def measure_median_runtime(algorithm, data, repetitions=5):
    recorded = []
    for _ in range(repetitions):
        t_start = time.perf_counter()
        algorithm(data)
        t_finish = time.perf_counter()
        recorded.append(t_finish - t_start)
    recorded.sort()
    return recorded[len(recorded) // 2]


def verify_correctness():
    validation_sets = [
        ("Empty Sequence", []),
        ("Single Element", [42.0]),
        ("Positive Values", [10, 20, 30, 40, 50]),
        ("Negative Values", [-3, -6, -9, -12]),
        ("Mixed Values", [15.5, -4.5, 22.0, -10.0, 5.0]),
    ]
    print("Algorithm Correctness Validation:")
    for label, seq in validation_sets:
        out1 = prefix_average1(seq)
        out2 = prefix_average2(seq)
        matches = len(out1) == len(out2) and all(
            math.isclose(x, y, rel_tol=1e-9) for x, y in zip(out1, out2)
        )
        status = "PASSED" if matches else "FAILED"
        rounded = [round(v, 2) for v in out2]
        print(f"  {label:<18}: {status} -> {rounded}")


def benchmark_performance():
    print("\nPerformance Benchmarking (prefix_average1 vs prefix_average2):")
    sample_sizes = [500, 1000, 2000, 4000, 8000]
    for n in sample_sizes:
        test_input = [random.uniform(1.0, 100.0) for _ in range(n)]
        t_quad = measure_median_runtime(prefix_average1, test_input)
        t_lin = measure_median_runtime(prefix_average2, test_input)
        ratio = t_quad / t_lin if t_lin > 0 else 0
        print(f"  n = {n:<5} | O(n^2): {t_quad:.6f} s | O(n): {t_lin:.6f} s | Speedup: {ratio:.1f}x")


if __name__ == "__main__":
    verify_correctness()
    benchmark_performance()
