
import time

# Sorting Algorithms

def timing_decorator(func):
    def wrapper(arr):
        start_time = time.perf_counter()
        f = func(arr)
        end_time = time.perf_counter()
        print(func.__name__)
        print("Time taken: {:.3e}".format(end_time-start_time))
        return f
    return wrapper

# Bubble Sort
@timing_decorator
def bubble_sort(arr):
    for x in range(len(arr)):
        for y in range(len(arr)-1-x):
            if arr[y] > arr[y+1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]
    return arr

# Insertion Sort
@timing_decorator
def insertion_sort(arr):
    for x in range(1, len(arr)):
        y = x
        while y > 0 and arr[y-1] > arr[y]:
            arr[y-1], arr[y] = arr[y], arr[y-1]
            y -= 1
    return arr

if __name__ == '__main__':
    arr = [3, 2, 13, 4, 6, 5, 7, 8, 1, 20]
    print(bubble_sort(arr))
    print(insertion_sort(arr))

    