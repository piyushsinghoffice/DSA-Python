import time
import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        curr_min_idx = i
        for j in range(i + 1, n):   # start from i+1
            if arr[j] < arr[curr_min_idx]:
                curr_min_idx = j
        
        arr[i], arr[curr_min_idx] = arr[curr_min_idx], arr[i]
    
    return arr

if __name__ == "__main__":
    arr = list(range(1,50))
    
    random.shuffle(arr)

    print("Unsorted Array: ", arr)

    start = time.time()
    arr = selection_sort(arr)
    end = time.time()
    
    print("Sorted Array: ", arr)
    print(f"Total time: {(end-start):.2f}")