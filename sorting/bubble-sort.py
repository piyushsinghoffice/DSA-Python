import time
import random

def bubble_sort(arr):
    size = len(arr)
    for i in range(size):
        swapped = False
        for j in range(0, size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    arr = list(range(1,10000))
    
    random.shuffle(arr)

    # print("Unsorted Array: ", arr)

    start = time.time()
    arr = bubble_sort(arr)
    end = time.time()
    
    # print("Sorted Array: ", arr)
    print(f"Total time: {(end-start):.2f}")