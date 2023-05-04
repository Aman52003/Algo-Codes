def mergeSort(array):
    if len(array) > 1:

        split = len(array)//2
        L = array[:split]
        R = array[split:]
      
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
       
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

      
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

array = [6, 5, 12, 10, 9, 1]

mergeSort(array)

print("Sorted array is: ")

for i in range(len(array)):
        print(array[i], end=" ")