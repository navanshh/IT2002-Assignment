# Navansh Mandowara - 25BEC066
# Lab 1: Benchmarking Algorithmic Growth Rates

import time
import math
import random


def constant_lookup(sequence, index):
    return sequence[index]


def binary_search(ordered_list, target):
    start = 0
    end = len(ordered_list) - 1
    while start <= end:
        midpoint = (start + end) // 2
        if ordered_list[midpoint] == target:
            return midpoint
        elif ordered_list[midpoint] < target:
            start = midpoint + 1
        else:
            end = midpoint - 1
    return -1


def linear_scan(elements, target):
    for idx, val in enumerate(elements):
        if val == target:
            return idx
    return -1


def merge_sort(items):
    if len(items) <= 1:
        return items
    pivot = len(items) // 2
    left_part = merge_sort(items[:pivot])
    right_part = merge_sort(items[pivot:])

    merged = []
    p1 = p2 = 0
    while p1 < len(left_part) and p2 < len(right_part):
        if left_part[p1] <= right_part[p2]:
            merged.append(left_part[p1])
            p1 += 1
        else:
            merged.append(right_part[p2])
            p2 += 1
    merged.extend(left_part[p1:])
    merged.extend(right_part[p2:])
    return merged


def count_positive_pairs(arr):
    total = 0
    sz = len(arr)
    for i in range(sz):
        for j in range(i + 1, sz):
            if arr[i] + arr[j] > 0:
                total += 1
    return total


def enumerate_subsets(seq):
    all_subsets = [[]]
    for element in seq:
        all_subsets += [current + [element] for current in all_subsets]
    return all_subsets


def measure_median_time(func, *args, trials=5):
    timings = []
    for _ in range(trials):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        timings.append(end_time - start_time)
    timings.sort()
    return timings[len(timings) // 2]


def run_growth_benchmarks():
    print("1. Constant Time O(1) - Index Access")
    for size in [10000, 50000, 100000, 250000, 500000]:
        test_seq = list(range(size))
        elapsed = measure_median_time(constant_lookup, test_seq, size // 2)
        print(f"  n = {size:<8} | Time: {elapsed:.8f} s")

    print("\n2. Logarithmic Time O(log n) - Binary Search")
    for size in [10000, 50000, 100000, 250000, 500000]:
        test_seq = list(range(size))
        elapsed = measure_median_time(binary_search, test_seq, -1)
        ratio = elapsed / math.log2(size)
        print(f"  n = {size:<8} | Time: {elapsed:.8f} s | T / log2(n): {ratio:.2e}")

    print("\n3. Linear Time O(n) - Linear Scan")
    for size in [10000, 50000, 100000, 200000, 400000]:
        test_seq = list(range(size))
        elapsed = measure_median_time(linear_scan, test_seq, -1)
        ratio = elapsed / size
        print(f"  n = {size:<8} | Time: {elapsed:.8f} s | T / n: {ratio:.2e}")

    print("\n4. Linearithmic Time O(n log n) - Merge Sort")
    for size in [1000, 2000, 4000, 8000, 16000]:
        test_seq = [random.randint(1, 100000) for _ in range(size)]
        elapsed = measure_median_time(merge_sort, test_seq)
        ratio = elapsed / (size * math.log2(size))
        print(f"  n = {size:<8} | Time: {elapsed:.8f} s | T / (n log2 n): {ratio:.2e}")

    print("\n5. Quadratic Time O(n^2) - Pair Counter")
    for size in [200, 400, 800, 1600, 3200]:
        test_seq = [random.randint(-100, 100) for _ in range(size)]
        elapsed = measure_median_time(count_positive_pairs, test_seq)
        ratio = elapsed / (size ** 2)
        print(f"  n = {size:<8} | Time: {elapsed:.8f} s | T / n^2: {ratio:.2e}")

    print("\n6. Exponential Time O(2^n) - Subset Enumeration")
    for size in [10, 12, 14, 16, 18, 20]:
        test_seq = list(range(size))
        elapsed = measure_median_time(enumerate_subsets, test_seq, trials=3)
        ratio = elapsed / (2 ** size)
        print(f"  n = {size:<8} | Time: {elapsed:.8f} s | T / 2^n: {ratio:.2e}")

    print("\nComplexity Summary:")
    summary_data = [
        ("Index Access", "O(1)", "Instantaneous memory reference"),
        ("Binary Search", "O(log n)", "Repeated search space halving"),
        ("Linear Scan", "O(n)", "Scales directly with list size"),
        ("Merge Sort", "O(n log n)", "Divide and conquer efficiency"),
        ("Pair Counter", "O(n^2)", "Time quadruples when n doubles"),
        ("Subsets Enum", "O(2^n)", "Time doubles with every element"),
    ]
    for name, bound, behavior in summary_data:
        print(f"  {name:<16} | {bound:<10} | {behavior}")


if __name__ == "__main__":
    run_growth_benchmarks()
