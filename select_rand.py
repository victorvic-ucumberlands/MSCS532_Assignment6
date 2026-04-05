#i-th element selection algorithm with pivot selected randomly from the subarray

import random

#partition function: rearrange the elements around the pivot and return the index of the pivot after partitioning
#args:
#A: array to be partitioned
#p: starting index of the subarray to be partitioned
#r: ending index of the subarray to be partitioned

def partition_random(A, p, r):
    #Random step: select a random pivot and swap it with the last element
    pivot_idx = random.randint(p, r)
    #Swap the pivot with the last element to reuse the paritioning logic from the original partition implementation
    tmp_val = A[pivot_idx]
    A[pivot_idx] = A[r]
    A[r] = tmp_val
    
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            #Add element to the left of the pivot
            i = i + 1
            #Swap arr[i] and arr[j]
            tmp_val = A[i]
            A[i] = A[j]
            A[j] = tmp_val

    #Swap the pivot so it goes to the right of the low side
    tmp_val = A[i + 1]
    A[i + 1] = A[r]
    A[r] = tmp_val

    return i + 1

#randomized-select function
#Call randomized partition to get the pivot index, and then recursively call randomized-select on the appropriate subarray depending on the value of k
#Args:
#A: array to select from
#p: starting index of the subarray to select from
#r: ending index of the subarray to select from
#i: the rank of the element to select

def randomized_select(A, p, r, i):
    if p == r:
        return A[p]

    q = partition_random(A, p, r)
    k = q - p + 1

    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)

#Entry point of the program: accept a csv file containing an array and an integer i representing the ith smallest element to be selected, and output the selected element to the console
if __name__ == "__main__":
    import csv
    #Memory profiler
    import tracemalloc
    #Time profiler
    import time

    import sys

    if len(sys.argv) != 3:
        print("Usage: python select_rand.py <input_csv_file> <i>")
        sys.exit(1)

    input_csv_file = sys.argv[1]
    i = int(sys.argv[2])

    with open(input_csv_file, 'r') as f:
        reader = csv.reader(f)
        arr = list(map(int, next(reader)))

    #Check if i is within the valid range
    if i < 1 or i > len(arr):
        print(f"Error: i must be between 1 and {len(arr)}")
        sys.exit(1)

    tracemalloc.start()
    start_time = time.time()

    selected_element = randomized_select(arr, 0, len(arr) - 1, i)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Selected element: {selected_element}")

    #Write the stats to a file
    peak_kb = peak / 1024
    with open('stats.txt', 'w') as f:
        f.write(f"{end_time - start_time},{peak_kb}")  


