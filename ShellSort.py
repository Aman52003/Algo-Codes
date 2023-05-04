def shell_sort(arr):
    # Start with a large gap, then reduce the gap until it is 1
    n = len(arr)
    gap = n // 2
    while gap > 0:
        # Do a gapped insertion sort for this gap size.
        # The first gap elements arr[0..gap-1] are already in gapped order
        for i in range(gap, n):
            # Add arr[i] to the elements that have been gap sorted
            # Save arr[i] in temp and make a hole at position i
            temp = arr[i]
            j = i
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            # Put temp (the original arr[i]) in its correct location
            arr[j] = temp
        # Reduce the gap for the next round
        gap //= 2
    return arr
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = shell_sort(arr)
print(sorted_arr) # [1, 2, 5, 5, 6, 9]
