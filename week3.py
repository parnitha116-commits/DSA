'''def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


n = int(input("Enter no. of elements: "))

if n <= 0:
    print("Number of elements must be positive")
else:
    arr = []

    print("Enter elements:")
    for i in range(n):
        arr.append(int(input()))

    bubble_sort(arr)

    print("Sorted Array:")
    for element in arr:
        print(element, end=" ")
'''
'''def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr


n = int(input("Enter no. of elements: "))
arr = []

print("Enter the elements:")

for i in range(n):
    arr.append(int(input()))

insertion_sort(arr)

print("Sorted Array:")

for element in arr:
    print(element, end=" ")
'''

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


n = int(input("Enter no. of elements: "))
arr = []

print("Enter the elements:")

for i in range(n):
    arr.append(int(input()))

print("Original Array:", arr)

selection_sort(arr)

print("Sorted Array:", arr)
































































    
