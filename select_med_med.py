#i-th element selection algorithm with pivot selected from the medians of medians algorithm
#partition-around function: parition based on a pivot value, which is the median of the medians of the subarray
#args:
#A: array to be partitioned
#p: starting index of the subarray to be partitioned
#r: ending index of the subarray to be partitioned
#x: the pivot value to partition around

def partition_around(A, p, r, x):
    #Find the index of the pivot value x in the subarray A[p..r]
    pivot_idx = -1
    for idx in range(p, r + 1):
        if A[idx] == x:
            pivot_idx = idx
            break
    
    if pivot_idx == -1:
        raise ValueError("Pivot value not found in the array")

    #Swap the pivot with the last element to reuse the paritioning logic from the original partition implementation
    tmp_val = A[pivot_idx]
    A[pivot_idx] = A[r]
    A[r] = tmp_val
    
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

#sort helper function: sort the subarray using insertion sort
#Insertion sort is fine since the subarrays are of size 5
#Args:
#A: array to be sorted
#idx: array containing the indeces of the elements to be sorted in place
def insertion_sort(A, idx):
    for j in range(1, len(idx)):
        key = A[idx[j]]
        i = j - 1
        while i >= 0 and A[idx[i]] > key:
            A[idx[i + 1]] = A[idx[i]]
            i = i - 1
        A[idx[i + 1]] = key
    

#select function: select the i-th smallest element from the subarray using the median of medians algorithm
#Args:
#A: array to select from
#p: starting index of the subarray to select from
#r: ending index of the subarray to select from
#i: the rank of the element to select

def select_med_med(A, p, r, i):
    #Reduce the array so it is divisible by 5. Put the smallest elements in the left side of the array and check if the elment that we want is in this group

    while (r - p + 1) % 5 != 0:
        #Put the smallest element in the left side of the array
        for j in range(p + 1, r + 1):
            if A[p] > A[j]:
                #Swap A[p] and A[j]
                tmp_val = A[p]
                A[p] = A[j]
                A[j] = tmp_val
        #Check if the element we want is the smallest element
        if i == 1:
            return A[p]

        #Otherwise, ingore the smallest element and continue with the rest of the array
        p = p + 1
        i = i - 1
    #Now the array is divisible by 5
    #Number of 5-element groups
    g = (r - p + 1) // 5

    #Sort each group 
    #At the end, the median of each group will be in the middle of the array
    for j in range(p, p + g ):
        idx_lst = [j, j + g, j + 2 * g, j + 3 * g, j + 4 * g]
        insertion_sort(A, idx_lst)

    #Now all the medians are in the middle of the array, so we can recursively call select to find the median of the medians
    #Next recursive step
    x = select_med_med(A, p + 2 * g, p + 3 * g - 1, g // 2 + 1)

    #Once the recursion returns, we have the median of the medians, so we can partition around this value and get its index
    q = partition_around(A, p, r, x)

    #Check if the pivot is the element we want
    k = q - p + 1

    if i == k:
        return A[q]
    
    elif i < k:
        return select_med_med(A, p, q - 1, i)
    else:
        return select_med_med(A, q + 1, r, i - k)









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

    selected_element = select_med_med(arr, 0, len(arr) - 1, i)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Selected element: {selected_element}")

    #Write the stats to a file
    peak_kb = peak / 1024
    with open('stats.txt', 'w') as f:
        f.write(f"{end_time - start_time},{peak_kb}")  


