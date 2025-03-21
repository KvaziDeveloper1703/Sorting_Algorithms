'''
The Selection Sort algorithm is a simple sorting method that divides the array into a sorted and an unsorted part. On each iteration, it finds the minimum element from the unsorted part and swaps it with the first unsorted element.

In this implementation:
+ The outer loop iterates over each element of the array.
+ The inner loop finds the index of the smallest element in the remaining unsorted part.
+ If the minimum element is different from the current one, they are swapped.

Алгоритм сортировки выбором — это простой метод сортировки, при котором массив последовательно делится на отсортированную и неотсортированную части. На каждом шаге из неотсортированной части выбирается минимальный элемент, который затем обменивается местами с первым элементом неотсортированной части.

В данной реализации:
+ Внешний цикл проходит по каждому элементу массива.
+ Внутренний цикл находит индекс минимального элемента в оставшейся части массива.
+ Если минимальный элемент отличается от текущего, происходит обмен.
'''

def selection_sort(given_array):
    N = len(given_array)
    for i in range(N):
        min_index = i
        for j in range(i + 1, N):
            if given_array[j] < given_array[min_index]:
                min_index = j
        if min_index != i:
            given_array[i], given_array[min_index] = given_array[min_index], given_array[i]
    return given_array

if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", sample_array)
    sorted_array = selection_sort(sample_array)
    print("Sorted array:", sorted_array)