'''
Merge Sort is an efficient sorting algorithm based on the divide and conquer principle. It divides the array into two halves, recursively sorts each half, and then merges them back into a single sorted array.

How the algorithm works:
+ If the array length is 1 or less, it's already sorted.
+ The array is split in half.
+ Each half is recursively sorted using merge_sort.
+ The sorted halves are combined using the merge function, which merges them into a sorted array.

Сортировка слиянием — это эффективный алгоритм сортировки, основанный на принципе разделяй и властвуй. Он делит массив на две части, рекурсивно сортирует каждую из них, а затем сливает их в один отсортированный массив.

Как работает алгоритм:
+ Если длина массива меньше или равна 1, он уже отсортирован.
+ Массив делится пополам.
+ Каждая половина сортируется рекурсивно с помощью merge_sort.
+ Отсортированные половины объединяются функцией merge, которая сливает их в один отсортированный массив.
'''

def merge_sort(given_array):
    if len(given_array) <= 1:
        return given_array

    mid = len(given_array) // 2
    left_half = merge_sort(given_array[:mid])
    right_half = merge_sort(given_array[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", sample_array)
    sorted_array = merge_sort(sample_array)
    print("Sorted array:", sorted_array)