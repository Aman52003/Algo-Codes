def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_side = arr[:mid]
        right_side = arr[mid:]

        merge_sort(left_side)
        merge_sort(right_side)

        i=j=k=0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                arr[k] = left_side[i]
                i +=1
            else:
                arr[k] = right_side[j]
                j +=1
            k +=1
        
        while i < len(left_side):
            arr[k] = left_side[i]
            i+= 1
            k+= 1

            while j < len(right_side):
                arr[k] = right_side[j]
                j+= 1
                k+= 1
    return arr

if __name__ == '__main__':
    arr = list(map(int, input("Enter a list of numbers to sort, separated by spaces: ").strip().split()))
    sorted_arr = merge_sort(arr)
    print("Sorted list: ", sorted_arr)


"""
    explaination

    The first line if __name__ == '__main__': is used in Python to specify that the code below it should be executed only if the script is being run as a standalone program and not imported as a module into another program.

The second line arr = list(map(int, input("Enter a list of numbers to sort, separated by spaces: ").strip().split())) takes user input as a string of space-separated numbers, strips any whitespace characters from the beginning and end of the string, splits the string into a list of strings based on the spaces, and maps each element of the list to an integer. The result is stored in the variable arr.

The third line sorted_arr = merge_sort(arr) calls the merge_sort function with the arr variable as an argument and stores the returned sorted list in the variable sorted_arr.

The last line print("Sorted list: ", sorted_arr) prints the sorted list stored in sorted_arr."""

'''def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

if __name__ == '__main__':
    with open('E:\Algorithams\number.txt', 'r') as f:
        number = [int(line.strip()) for line in f]
        sorted_numbers = merge_sort(number)
        print(sorted_numbers)

    '''