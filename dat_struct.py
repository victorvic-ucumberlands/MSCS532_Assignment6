#This script implements the elementary data structures
#To implement the structs as arrays
import array 


#array
class Array:
    def __init__(self, size):
        self.arr = array.array('i', [0] * size)
        self.size = size
    
    def getitem(self, idx):
        return self.arr[idx]
    
    def setitem(self, idx, value):
        self.arr[idx] = value

    def len(self):
        return self.size
    
#Matrix
class Matrix:
    def __init__(self, num_rows, num_cols):
        self.mat = [array.array('i', [0] * num_cols) for _ in range(num_rows)]
        self.num_rows = num_rows
        self.num_cols = num_cols
    
    def getitem(self, row_idx, col_idx):
        return self.mat[row_idx][col_idx]
    
    def setitem(self, row_idx, col_idx, value):
        self.mat[row_idx][col_idx] = value

    def shape(self):
        return (self.num_rows, self.num_cols)

#Stack
class Stack:
    def __init__(self, size):
        self.stack = array.array('i', [0] * size)
        self.top = -1
        self.size = 0
        self.capacity = size
    def push(self, value):
        if self.size == self.capacity:
            raise IndexError("Stack overflow")
        self.top += 1
        self.stack[self.top] = value
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Stack underflow")
        value = self.stack[self.top]
        self.top -= 1
        self.size -= 1
        return value

#Queue
class Queue:
    def __init__(self, size):
        self.queue = array.array('i', [0] * size)
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = size
    
    def enqueue(self, value):
        if self.size == self.capacity:
            raise IndexError("Queue overflow")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Queue underflow")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value
    
#Linked List Node
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
    
    def getitem(self, idx):
        if idx < 0 or idx >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def setitem(self, idx, value):
        if idx < 0 or idx >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(idx):
            current = current.next
        current.value = value
    
    def insert(self, idx, value):
        if idx < 0 or idx > self.size:
            raise IndexError("Index out of bounds")
        new_node = ListNode(value)
        if idx == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
        elif idx == self.size:
            new_node.prev = self.tail
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            for _ in range(idx):
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
        self.size += 1

    def delete(self, idx):
        if idx < 0 or idx >= self.size:
            raise IndexError("Index out of bounds")
        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            if self.size == 1:
                self.tail = None
        elif idx == self.size - 1:
            value = self.tail.value
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            current = self.head
            for _ in range(idx):
                current = current.next
            value = current.value
            current.prev.next = current.next
            current.next.prev = current.prev
        self.size -= 1
        return value

#Main function to test the data structures
if __name__ == "__main__":
    #Generate ranom arrays of different data sizes and test the data structures
    import random
    #Test array
    import numpy as np
    import time
    import sys

    arr1 = np.random.randint(0, 10000000, 100)
    arr2 = np.random.randint(0, 10000000, 1000)
    arr3 = np.random.randint(0, 10000000, 10000)
    arr4 = np.random.randint(0, 10000000, 100000)

    #Benchmark all item insertion, retrieval and deletion for each data structure, and graph the results using matplotlib
    array_insert_time = []
    array_retrieval_time = []
    array_deletion_time = []

    matrix_insert_time = []
    matrix_retrieval_time = []
    matrix_deletion_time = []

    stack_push_time = []
    #Pop is equal to deletion for stack
    stack_pop_time = []

    queue_enqueue_time = []
    #Dequeue is equal to deletion for queue
    queue_dequeue_time = []

    linked_list_insert_time = []
    linked_list_retrieval_time = []
    linked_list_deletion_time = []


    for arr in [arr1, arr2, arr3, arr4]:
        #Test array
        print(f"Testing array of size {len(arr)}")
        array_i = Array(len(arr))
        start_time = time.time()
        for i in range(len(arr)):
            array_i.setitem(i, arr[i])
        end_time = time.time()
        array_insert_time.append(end_time - start_time)

        start_time = time.time()
        for i in range(len(arr)):
            _ = array_i.getitem(i)
        end_time = time.time()
        array_retrieval_time.append(end_time - start_time)

        start_time = time.time()
        for i in range(len(arr)):
            array_i.setitem(i, 0)
        end_time = time.time()
        array_deletion_time.append(end_time - start_time)

        #Test matrix
        print(f"Testing matrix of size {len(arr)}")
        num_rows = int(len(arr) ** 0.5)
        num_cols = int(len(arr) ** 0.5)
        matrix = Matrix(num_rows, num_cols)
        start_time = time.time()
        for i in range(num_rows):
            for j in range(num_cols):
                matrix.setitem(i, j, arr[i * num_cols + j])
        end_time = time.time()
        matrix_insert_time.append(end_time - start_time)

        start_time = time.time()
        for i in range(num_rows):
            for j in range(num_cols):
                _ = matrix.getitem(i, j)
        end_time = time.time()
        matrix_retrieval_time.append(end_time - start_time)

        start_time = time.time()
        for i in range(num_rows):
            for j in range(num_cols):
                matrix.setitem(i, j, 0)
        end_time = time.time()
        matrix_deletion_time.append(end_time - start_time)

        #Test stack
        print(f"Testing stack of size {len(arr)}")

        stack = Stack(len(arr))
        start_time = time.time()
        for i in range(len(arr)):
            stack.push(arr[i])
        end_time = time.time()
        stack_push_time.append(end_time - start_time)


        start_time = time.time()
        for i in range(len(arr)):
            stack.pop()
        end_time = time.time()
        stack_pop_time.append(end_time - start_time)

        #Test queue
        print(f"Testing queue of size {len(arr)}")
        queue = Queue(len(arr))
        start_time = time.time()
        for i in range(len(arr)):
            queue.enqueue(arr[i])
        end_time = time.time()
        queue_enqueue_time.append(end_time - start_time)

        start_time = time.time()
        for i in range(len(arr)):
            queue.dequeue()
        end_time = time.time()
        queue_dequeue_time.append(end_time - start_time)

        #Test linked list
        print(f"Testing linked list of size {len(arr)}")
        linked_list = LinkedList()
        start_time = time.time()
        for i in range(len(arr)):
            linked_list.append(arr[i])
        end_time = time.time()
        linked_list_insert_time.append(end_time - start_time)

        start_time = time.time()
        for i in range(len(arr)):
            _ = linked_list.getitem(i)
        end_time = time.time()
        linked_list_retrieval_time.append(end_time - start_time)  

        start_time = time.time()
        for i in range(len(arr)):
            linked_list.delete(0)
        end_time = time.time()
        linked_list_deletion_time.append(end_time - start_time)

    #Plot the results using matplotlib
    import matplotlib.pyplot as plt
    sizes = [100, 1000, 10000, 100000]
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, array_insert_time, marker='o', label='Array Insert')
    plt.plot(sizes, array_retrieval_time, marker='o', label='Array Retrieval')
    plt.plot(sizes, array_deletion_time, marker='o', label='Array Deletion')
    plt.xscale('log')
    plt.xlabel('Data Size (log scale)')
    plt.ylabel('Time (seconds)')
    plt.title('Array Operations Time Analysis')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, matrix_insert_time, marker='o', label='Matrix Insert')
    plt.plot(sizes, matrix_retrieval_time, marker='o', label='Matrix Retrieval')
    plt.plot(sizes, matrix_deletion_time, marker='o', label='Matrix Deletion')
    plt.xscale('log')
    plt.xlabel('Data Size (log scale)')
    plt.ylabel('Time (seconds)')
    plt.title('Matrix Operations Time Analysis')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, stack_push_time, marker='o', label='Stack Push')
    plt.plot(sizes, stack_pop_time, marker='o', label='Stack Pop')
    plt.xscale('log')
    plt.xlabel('Data Size (log scale)')
    plt.ylabel('Time (seconds)')
    plt.title('Stack Operations Time Analysis')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, queue_enqueue_time, marker='o', label='Queue Enqueue')
    plt.plot(sizes, queue_dequeue_time, marker='o', label='Queue Dequeue')
    plt.xscale('log')
    plt.xlabel('Data Size (log scale)')
    plt.ylabel('Time (seconds)')
    plt.title('Queue Operations Time Analysis')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linked_list_insert_time, marker='o', label='Linked List Insert')
    plt.plot(sizes, linked_list_retrieval_time, marker='o', label='Linked List Retrieval')
    plt.plot(sizes, linked_list_deletion_time, marker='o', label='Linked List Deletion')
    plt.xscale('log')
    plt.xlabel('Data Size (log scale)')
    plt.ylabel('Time (seconds)')
    plt.title('Linked List Operations Time Analysis')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()

    #Write the stats to a text file
    with open('data_struct_stats.txt', 'w') as f:
        f.write("Data Size,Array Insert,Array Retrieval,Array Deletion,Matrix Insert,Matrix Retrieval,Matrix Deletion,Stack Push,Stack Pop,Queue Enqueue,Queue Dequeue,Linked List Insert,Linked List Retrieval,Linked List Deletion\n")
        for i in range(len(sizes)):
            f.write(f"{sizes[i]},{array_insert_time[i]},{array_retrieval_time[i]},{array_deletion_time[i]},{matrix_insert_time[i]},{matrix_retrieval_time[i]},{matrix_deletion_time[i]},{stack_push_time[i]},{stack_pop_time[i]},{queue_enqueue_time[i]},{queue_dequeue_time[i]},{linked_list_insert_time[i]},{linked_list_retrieval_time[i]},{linked_list_deletion_time[i]}\n")
    
    







    