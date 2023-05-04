array = [13,87,6,40,23]

temp = 0

for i in range (len(array)):
    for j in range (0, len(array)-i-1):
        if(array[j] > array[j+1]):
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp


for i in array:
    print(i)
