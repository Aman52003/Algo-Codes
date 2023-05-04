def divide (arr, low, high) :
    pivot = arr[high]
    i = low-1
    
    for j in range (low,high):
        if(arr[j]<=pivot):
            i = i + 1
            temp = arr[i]
            arr[i]= arr[j]
            arr[j] = temp
            
 
    temp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = temp
    return i + 1

def quick(array, low, high):
    if low < high:
 
        
        pi = divide(array, low, high)
 
        
        quick(array, low, pi - 1)
 
      
        quick(array, pi + 1, high)



arr = [8,12,24,3,36,80,19,40]
low = 0
high = len(arr)-1

quick(arr,low,high)
print(f'{arr}')
