def binary_search(arr, n):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [13,87,6,40,23]
temp = 0

for i in range(len(arr)) :
    min = i
    for j in range(i+1,len(arr)):
        if(arr[min]>arr[j]):
            min = j
    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp


n = int(input("Enter the number you want to search for: "))
result = binary_search(arr, n)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in the array")