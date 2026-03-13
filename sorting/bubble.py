def bubbleSort(collection):
    n = len(collection)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i): # the last i elements of the array is already sorted
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swapped = True

        if not swapped: # if the array is already sorted loop will break after first time
            break
    return collection


arr = [64, 25, 12, 22, 11]
newArr = bubbleSort(arr[:])

print(f"Unsorted array: {arr}")
print(f"Sorted array: {newArr}")