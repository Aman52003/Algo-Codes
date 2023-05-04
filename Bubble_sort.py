
def bubble_sort(Item):
    total_iteration = 0
    for i in range(0,len(Item)-1):
        for j in range(len(Item)-1):
            if(Item[j]>Item[j+1]):
                Item[j],Item[j+1] = Item[j+1],Item[j]
            total_iteration +=1
    print("total itration = " , total_iteration)
    return Item

Item = []
n  = int(input("enter size = "))

for i in range(0,n):
    itm = int(input())
    Item.append(itm)

print("Unsorted list = ", Item)
print("sorted list = ", bubble_sort(Item))
