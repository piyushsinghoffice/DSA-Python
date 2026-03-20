import time
import random

def insertion_sort(arr, watch=False):
    size = len(arr)
    for i in range(1,size):
        j = i
        if watch:
            print(f"i: {i}, j: {j}")
        while j>0 and arr[j-1]>arr[j]:
            if watch:
                print(f"\ti: [{arr[j-1]}] <-> j: [{arr[j]}]")
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j = j-1
    
    return arr


if __name__ == "__main__":
    arr = list(range(1,20))
    
    random.shuffle(arr)

    print("Unsorted Array: ", arr)

    start = time.time()
    arr = insertion_sort(arr, watch=False)
    end = time.time()
    
    print("Sorted Array: ", arr)
    print(f"Total time: {(end-start):.2f}")