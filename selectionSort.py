array = [13,87,6,40,23]


temp = 0

for i in range(len(array)) :
    min = i
    for j in range(i+1,len(array)):
        if(array[min]>array[j]):
            min = j
    temp = array[i]
    array[i] = array[min]
    array[min] = temp

for i in array:
    print(i)

