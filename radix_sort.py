'''
Radix Sort is a non-comparison-based sorting algorithm that sorts numbers digit by digit, starting from the least significant digit (units place) and moving toward the most significant digit. For sorting by each digit, it uses Counting Sort, which is stable.

How the algorithm works:
+ The maximum value in the array is found to determine the number of digits.
+ Sorting is done for each digit place (1, 10, 100, etc.) using the helper function counting_sort_by_digit.
+ Each pass sorts the array based on the current digit, preserving the order of previous digits.

Поразрядная сортировка — это некомпаративный алгоритм сортировки, который сортирует числа поразрядно, начиная с младшего разряда (единиц) и переходя к старшему. Для сортировки по каждому разряду используется сортировка подсчётом, так как она стабильна.

Как работает алгоритм:
+ Определяется максимальное значение в массиве, чтобы узнать количество разрядов.
+ Сортировка выполняется по каждой цифре (1, 10, 100 и т. д.), с использованием вспомогательной функции counting_sort_by_digit.
+ Каждый проход упорядочивает массив по текущему разряду, сохраняя уже отсортированные предыдущие разряды.
'''

def counting_sort_by_digit(given_array, digit_place):
    N = len(given_array)
    output = [0] * N
    count = [0] * 10

    for number in given_array:
        digit = (number // digit_place) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(N - 1, -1, -1):
        digit = (given_array[i] // digit_place) % 10
        count[digit] -= 1
        output[count[digit]] = given_array[i]

    return output

def radix_sort(given_array):
    if not given_array:
        return given_array

    max_value = max(given_array)
    digit_place = 1

    while max_value // digit_place > 0:
        given_array = counting_sort_by_digit(given_array, digit_place)
        digit_place *= 10

    return given_array

if __name__ == "__main__":
    sample_array = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original array:", sample_array)
    sorted_array = radix_sort(sample_array)
    print("Sorted array:", sorted_array)