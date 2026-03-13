def selectionSort(collection):
    n = len(collection)
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if collection[minIndex] > collection[j]:
                minIndex = j
        collection[i], collection[minIndex] = collection[minIndex], collection[i]

    return collection


arr = [64, 25, 12, 22, 11]
newArr = selectionSort(arr[:])

print(f"Unsorted arr: {arr}")
print(f"Sorted arr: {newArr}")