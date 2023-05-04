def heap_sort(arr):
    # Build a max heap
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # swap
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    # Build a max heap recursively from a given node i
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)
arr = [5, 2, 9, 1, 5, 6, 7, 10, 11]
sorted_arr = heap_sort(arr)
print(sorted_arr) # [1, 2, 5, 5, 6, 9, 7, 10, 11]
