'''
Quick Sort is one of the most efficient sorting algorithms, based on the divide and conquer strategy. The core idea is to choose a pivot element and partition the array into two parts:
    - Elements less than or equal to the pivot / Elements greater than the pivot;
    - Then, each part is recursively sorted and combined as: sorted_less + [pivot] + sorted_greater.

In this implementation:
    - The first element is chosen as the pivot;
    - The array is split using list comprehensions;
    - Sorting continues recursively on each part.

Быстрая сортировка - это один из самых эффективных алгоритмов сортировки, использующий стратегию разделяй и властвуй. Основная идея - выбрать опорный элемент (pivot) и разделить массив на две части:
    - Элементы меньше или равные опорному / Элементы больше опорного;
    - Затем каждая из частей сортируется рекурсивно, и результат объединяется: отсортованные_меньшие + [опорный] + отсортованные_большие.

В данной реализации:
    - В качестве опорного элемента выбран первый элемент массива;
    - Массив разбивается на две части с помощью генераторов списков;
    - Сортировка продолжается рекурсивно для обеих частей.

Pikalajittelu (quick sort) on yksi tehokkaimmista lajittelualgoritmeista, ja se perustuu “jako ja hallitse” -strategiaan. Perusidea on valita pivot-alkio (operoiva alkio) ja jakaa taulukko kahteen osaan:
    - alkiot, jotka ovat pienempiä tai yhtä suuria kuin pivot, sekä alkiot, jotka ovat suurempia kuin pivot;
    - Tämän jälkeen molemmat osat lajitellaan rekursiivisesti, ja tulokset yhdistetään: lajitellut_pienemmät + [pivot] + lajitellut_suuremmat.

Tässä toteutuksessa:
    - Pivot-alkioksi valitaan taulukon ensimmäinen alkio;
    - Taulukko jaetaan kahteen osaan listageneraattoreiden avulla;
    - Lajittelu jatkuu rekursiivisesti molemmille osille.
'''

def quick_sort(given_array):
    if len(given_array) <= 1:
        return given_array

    pivot = given_array[0]
    less = [number for number in given_array[1:] if number <= pivot]
    greater = [number for number in given_array[1:] if number > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", sample_array)
    sorted_array = quick_sort(sample_array)
    print("Sorted array:", sorted_array)