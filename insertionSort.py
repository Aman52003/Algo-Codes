array = [13,87,6,40,23]

temp = 0

for i in range(len(array)):
    for j in range(i+1):
        if(array[i]>array[j]):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            # print(array[i])

for i in array:
    print(i)

