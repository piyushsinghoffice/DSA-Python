import time
import random

def partition(a, l, h):
    pivot = a[l]
    i = l - 1
    j = h + 1
    
    while True:
        i += 1
        while a[i] < pivot:
            i += 1
        
        j -= 1
        while a[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        a[i], a[j] = a[j], a[i]


def quick_sort(a, l, h):
    if l < h:
        j = partition(a, l, h)
        quick_sort(a, l, j)
        quick_sort(a, j + 1, h)

if __name__ == "__main__":
    arr = list(range(1,10))
    
    random.shuffle(arr)

    print("Unsorted Array: ", arr)

    start = time.time()
    quick_sort(arr, 0, len(arr)-1)
    end = time.time()
    
    print("Sorted Array: ", arr)
    print(f"Total time: {(end-start):.2f}")