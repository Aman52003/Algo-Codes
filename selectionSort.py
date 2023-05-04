def selection_sort(arr):
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element {}: ".format(i+1))))
selection_sort(arr)
print("Sorted array:", arr)
