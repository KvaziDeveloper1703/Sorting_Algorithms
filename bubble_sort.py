'''
The Bubble Sort algorithm is a simple sorting technique that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is completely sorted.

In this implementation:
+ The outer loop controls the number of passes through the array.
+ The inner loop compares and swaps adjacent elements as needed.
+ The swapped flag is used for optimization: if no swaps are made during a full pass, the algorithm stops early, as the array is already sorted.

Алгоритм сортировки пузырьком — это простой алгоритм сортировки, который многократно проходит по списку, сравнивая попарно соседние элементы и меняя их местами, если они стоят в неправильном порядке. Этот процесс продолжается до тех пор, пока список не будет полностью отсортирован.

В данной реализации:
+ Внешний цикл отвечает за количество проходов по массиву.
+ Внутренний цикл сравнивает пары элементов и меняет их местами, если требуется.
+ Флаг swapped используется для оптимизации: если за один проход не произошло ни одной перестановки, алгоритм завершает работу раньше, так как массив уже отсортирован.
'''

def bubble_sort(given_array):
    N = len(given_array)
    for i in range(N - 1):
        swapped = False
        for j in range(N - i - 1):
            if given_array[j] > given_array[j + 1]:
                given_array[j], given_array[j + 1] = given_array[j + 1], given_array[j]
                swapped = True
        if not swapped:
            break
    return given_array

if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", sample_array)
    sorted_array = bubble_sort(sample_array)
    print("Sorted array:", sorted_array)