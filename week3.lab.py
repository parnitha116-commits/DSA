def bubble_sort(arr):
    n = len(arr)
 
    for i in range(n):
               swapped = False
 
        for j in range(0, n - i - 1)
            if arr[j] > arr[j + 1]:
               
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
 
       
        if not swapped:
            break
 
    return arr
 
 

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
 
print("Sorted array:", sorted_numbers)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
 
       
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
 
        
        arr[j + 1] = key
 
    return arr
 
 
numbers = [64, 34, 25, 12, 22, 11, 90]
 
print("Sorted array:", insertion_sort(numbers))

def selection_sort(arr):

    n = len(arr)
 
    for i in range(n):

        min_index = i
 
        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:

                min_index = j
 

        

        arr[i], arr[min_index] = arr[min_index], arr[i]
 
    return arr
 
 
numbers = [64, 25, 12, 22, 11]
 
print("Sorted array:", selection_sort(numbers))





def selection_sort(arr):

    n = len(arr)
 
    for i in range(n):

        min_index = i
 
        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:

                min_index = j
 


        arr[i], arr[min_index] = arr[min_index], arr[i]
 
    return arr
 
 
numbers = [64, 25, 12, 22, 11]
 
print("Sorted array:", selection_sort(numbers))









 def quick_sort(arr):

    if len(arr) <= 1:

        return arr
 
    pivot = arr[-1]
 
    left = []

    right = []
 
    for i in range(len(arr) - 1):

        if arr[i] < pivot:

            left.append(arr[i])

        else:

            right.append(arr[i])
 
    return quick_sort(left) + [pivot] + quick_sort(right)
 
 
numbers = [10, 7, 8, 9, 1, 5]
 
print("Sorted array:", quick_sort(numbers))
 




 




















