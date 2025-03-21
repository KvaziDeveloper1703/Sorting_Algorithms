'''
Insertion Sort is a simple and intuitive sorting algorithm that works by inserting each element into its correct position within the already sorted part of the array.

In this implementation:
+ The first element is considered sorted.
+ For each iteration, the current element (key) is compared to the elements to its left.
+ If those elements are greater than key, they are shifted one position to the right.
+ Once the correct position is found, key is inserted there.

Сортировка вставками — это простой и интуитивно понятный алгоритм сортировки, который работает по принципу вставки каждого элемента на нужное место в уже отсортированной части массива.

В данной реализации:
+ Считается, что первый элемент уже отсортирован.
+ На каждой итерации текущий элемент (key) сравнивается с элементами слева от него.
+ Если элементы слева больше key, они сдвигаются вправо.
+ Когда находится нужное место, key вставляется на своё место.
'''

def insertion_sort(given_array):
    N = len(given_array)
    for i in range(1, N):
        key = given_array[i]
        j = i - 1
        while j >= 0 and given_array[j] > key:
            given_array[j + 1] = given_array[j]
            j -= 1
        given_array[j + 1] = key
    return given_array

if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", sample_array)
    sorted_array = insertion_sort(sample_array)
    print("Sorted array:", sorted_array)