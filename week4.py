'''def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


n = int(input("Enter number of elements: "))
arr = []

print("Enter elements:")

for i in range(n):
    arr.append(int(input()))

merge_sort(arr)

print("Sorted Array:")
for element in arr:
    print(element, end=" ")'''

def quick_sort(a, low, high):
    if low < high:
        i = low
        j = high
        pivot = low

        while i < j:
            while i < len(a) and a[i] <= a[pivot]:
                i += 1

            while a[j] > a[pivot]:
                j -= 1

            if i < j:
                a[i], a[j] = a[j], a[i]

        a[j], a[pivot] = a[pivot], a[j]

        quick_sort(a, low, j - 1)
        quick_sort(a, j + 1, high)


a = list(map(int, input("Enter numbers to sort: ").split()))

quick_sort(a, 0, len(a) - 1)

print("Sorted Array:")
print(a)
















































