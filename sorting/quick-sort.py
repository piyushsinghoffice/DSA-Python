import time
import random

def partition(a, l, h):
    pivot = a[h]
    i = l - 1
    
    for j in range(l, h):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    
    a[i + 1], a[h] = a[h], a[i + 1]
    return i + 1


def quick_sort(a, l, h):
    if l < h:
        p = partition(a, l, h)
        quick_sort(a, l, p - 1)
        quick_sort(a, p + 1, h)

if __name__ == "__main__":
    arr = list(range(1,10000))
    
    random.shuffle(arr)

    print("Unsorted Array: ", arr)

    start = time.time()
    quick_sort(arr, 0, len(arr)-1)
    end = time.time()
    
    print("Sorted Array: ", arr)
    print(f"Total time: {(end-start):.2f}")