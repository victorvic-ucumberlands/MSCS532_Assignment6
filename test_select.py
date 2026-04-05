#This script generates random arrays of different sizes, and types (random, sorted, reverse-sorter, arrays with repeated elements)
#It then calls the impmentation of quick_sort_random,

import csv
import numpy as np

print("Generating random arrays")

arr1 = np.random.randint(0, 10000000, 10000)
arr2 = np.random.randint(0, 10000000, 100000)
arr3 = np.random.randint(0, 10000000, 1000000)
arr4 = np.random.randint(0, 10000000, 10000000)


#Sort arrays in ascending order using python's built-in sorted() function
print("Sorting arrays in ascending order")
sorted_arr1 = sorted(arr1)
sorted_arr2 = sorted(arr2)
sorted_arr3 = sorted(arr3)
sorted_arr4 = sorted(arr4)


#Sort arrays in descending order using python's built-in sorted() function
print("Sorting arrays in descending order")
sorted_arr1_desc = sorted(arr1, reverse=True)
sorted_arr2_desc = sorted(arr2, reverse=True)
sorted_arr3_desc = sorted(arr3, reverse=True)
sorted_arr4_desc = sorted(arr4, reverse=True)



#Measure time and memory usage of medians of medians select on each array
time_random = []
time_sorted = []
time_sorted_desc = []

memory_random = []
memory_sorted = []
memory_sorted_desc = []

#Measure time and memory usage of random select 
time_random_rnd = []
time_sorted_rnd = []
time_sorted_desc_rnd = []

memory_random_rnd = []
memory_sorted_rnd = []
memory_sorted_desc_rnd = []

# Measure time and memory usage of random select on each random array
print("Measuring time and memory usage of random select on random arrays")
for arr in [arr1, arr2, arr3, arr4]:
    #Write arr to a csv file
    with open('arr_random.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(arr)
    #Call select_rand.py on the csv file
    import subprocess
    #always select the median element, which is the n/2 th smallest element
    subprocess.run(['python3', 'select_rand.py', 'arr_random.csv', str(len(arr)//2)])  
    #Read the stats from the text file

    with open('stats.txt', 'r') as f:
        stats = f.read().split(',')
        time_random_rnd.append(float(stats[0]))
        memory_random_rnd.append(float(stats[1]))
    
    #For the median of medians implementation
    subprocess.run(['python3', 'select_med_med.py', 'arr_random.csv', str(len(arr)//2)])
    with open('stats.txt', 'r') as f:
        stats = f.read().split(',')
        time_random.append(float(stats[0]))
        memory_random.append(float(stats[1]))

#Save data to a csv file
with open('results_random.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Array Size', 'Time (s)', 'Memory (KB)'])
    for i in range(len(time_random)):
        writer.writerow([10**(i+4), time_random[i], memory_random[i]])
    

#Save data for random select to a csv file
with open('results_random_rnd.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Array Size', 'Time (s)', 'Memory (KB)'])
    for i in range(len(time_random_rnd)):
        writer.writerow([10**(i+4), time_random_rnd[i], memory_random_rnd[i]])










# Measure time and memory usage of random select on each sorted array (ascending)
print("Measuring time and memory usage of random select on sorted arrays (ascending)")
for arr in [sorted_arr1, sorted_arr2, sorted_arr3, sorted_arr4]:
    #Write arr to a csv file
    with open('arr_sorted.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(arr)
    #Call select_rand.py on the csv file
    import subprocess
    #always select the median element, which is the n/2 th smallest element
    subprocess.run(['python3', 'select_rand.py', 'arr_sorted.csv', str(len(arr)//2)])  
    #Read the stats from the text file

    with open('stats.txt', 'r') as f:
        stats = f.read().split(',')
        time_sorted_rnd.append(float(stats[0]))
        memory_sorted_rnd.append(float(stats[1]))
    
    #For the median of medians implementation
    subprocess.run(['python3', 'select_med_med.py', 'arr_sorted.csv', str(len(arr)//2)])
    with open('stats.txt', 'r') as f:
        stats = f.read().split(',')
        time_sorted.append(float(stats[0]))
        memory_sorted.append(float(stats[1]))

#Save data to a csv file
with open('results_sorted.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Array Size', 'Time (s)', 'Memory (KB)'])
    for i in range(len(time_sorted)):
        writer.writerow([10**(i+4), time_sorted[i], memory_sorted[i]])
    

#Save data for random select to a csv file
with open('results_sorted_rnd.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Array Size', 'Time (s)', 'Memory (KB)'])
    for i in range(len(time_sorted_rnd)):
        writer.writerow([10**(i+4), time_sorted_rnd[i], memory_sorted_rnd[i]])




# Measure time and memory usage of random select on each sorted array (descending)
print("Measuring time and memory usage of random select on sorted arrays (descending)")
for arr in [sorted_arr1_desc, sorted_arr2_desc, sorted_arr3_desc, sorted_arr4_desc]:
    #Write arr to a csv file
    with open('arr_sorted_desc.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(arr)
    #Call select_rand.py on the csv file
    import subprocess
    #always select the median element, which is the n/2 th smallest element
    subprocess.run(['python3', 'select_rand.py', 'arr_sorted_desc.csv', str(len(arr)//2)])  
    #Read the stats from the text file

    with open('stats.txt', 'r') as f:
        stats = f.read().split(',')
        time_sorted_desc_rnd.append(float(stats[0]))
        memory_sorted_desc_rnd.append(float(stats[1]))
    
    #For the median of medians implementation
    subprocess.run(['python3', 'select_med_med.py', 'arr_sorted_desc.csv', str(len(arr)//2)])
    with open('stats.txt', 'r') as f:
        stats = f.read().split(',')
        time_sorted_desc.append(float(stats[0]))
        memory_sorted_desc.append(float(stats[1]))

#Save data to a csv file
with open('results_sorted_desc.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Array Size', 'Time (s)', 'Memory (KB)'])
    for i in range(len(time_sorted_desc)):
        writer.writerow([10**(i+4), time_sorted_desc[i], memory_sorted_desc[i]])
    

#Save data for random select to a csv file
with open('results_sorted_desc_rnd.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Array Size', 'Time (s)', 'Memory (KB)'])
    for i in range(len(time_sorted_desc_rnd)):
        writer.writerow([10**(i+4), time_sorted_desc_rnd[i], memory_sorted_desc_rnd[i]])













#Plot the results using matplotlib
import matplotlib.pyplot as plt

sizes = [1e4, 1e5, 1e6, 1e7]
plt.figure(figsize=(10, 6))
plt.plot(sizes, time_random, marker='o', label='Random')
plt.plot(sizes, time_sorted, marker='o', label='Sorted Ascending')
plt.plot(sizes, time_sorted_desc, marker='o', label='Sorted Descending')
plt.xscale('log')
plt.xlabel('Array Size (log scale)')
plt.ylabel('Time (seconds)')
plt.title('Selection Algorithm (median of medians) Time Analysis')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()

#Plot memory usage
plt.figure(figsize=(10, 6))
plt.plot(sizes, memory_random, marker='o', label='Random')
plt.plot(sizes, memory_sorted, marker='o', label='Sorted Ascending')
plt.plot(sizes, memory_sorted_desc, marker='o', label='Sorted Descending')
plt.xscale('log')
plt.xlabel('Array Size (log scale)')
plt.ylabel('Memory Usage (KB)')
plt.title('Selection Algorithm (median of medians) Memory Usage Analysis')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()

#Plot the results for quick sort with random pivot selection using matplotlib
plt.figure(figsize=(10, 6))
plt.plot(sizes, time_random_rnd, marker='o', label='Random')
plt.plot(sizes, time_sorted_rnd, marker='o', label='Sorted Ascending')
plt.plot(sizes, time_sorted_desc_rnd, marker='o', label='Sorted Descending')
plt.xscale('log')
plt.xlabel('Array Size (log scale)')
plt.ylabel('Time (seconds)')
plt.title('Selection Algorithm (random pivot) Time Analysis')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()

#Plot memory usage for selection algorithm with random pivot
plt.figure(figsize=(10, 6))
plt.plot(sizes, memory_random_rnd, marker='o', label='Random')
plt.plot(sizes, memory_sorted_rnd, marker='o', label='Sorted Ascending')
plt.plot(sizes, memory_sorted_desc_rnd, marker='o', label='Sorted Descending')
plt.xscale('log')
plt.xlabel('Array Size (log scale)')
plt.ylabel('Memory Usage (KB)')
plt.title('Selection Algorithm (random pivot) Memory Usage Analysis')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()

