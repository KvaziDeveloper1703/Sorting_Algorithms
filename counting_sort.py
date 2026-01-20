'''
Counting Sort is a non-comparison-based sorting algorithm that works by counting the number of occurrences of each unique element. It is suitable only for integers within a limited range.

How the algorithm works:
    - The minimum and maximum values in the array are found;
    - A helper array count is created to store the count of each unique number;
    - The count array is then transformed into a prefix sum array, which determines positions of elements in the output;
    - The sorted array is built in reverse to maintain stability.

Сортировка подсчётом - это некомпаративный алгоритм сортировки, который работает за счёт подсчёта количества вхождений каждого уникального элемента. Подходит только для целых чисел в ограниченном диапазоне.

Как работает алгоритм:
    - Находятся минимальное и максимальное значения массива;
    - Создаётся вспомогательный массив count для хранения количества каждого значения;
    - Затем count преобразуется в массив префиксных сумм - он определяет позиции элементов в итоговом массиве;
    - Построение отсортированного массива осуществляется с конца.

Laskentalajittelu (counting sort) on ei-vertailuun perustuva lajittelualgoritmi, joka toimii laskemalla kunkin yksilöllisen alkion esiintymiskerrat. Se sopii vain kokonaisluvuille, jotka ovat rajatulla arvoalueella.

Miten algoritmi toimii:
    - Etsitään taulukon pienin ja suurin arvo;
    - Luodaan aputaulukko count, johon tallennetaan kunkin arvon esiintymismäärä;
    - Tämän jälkeen count muunnetaan prefiksisummataulukoksi, joka määrittää alkioiden paikat lopullisessa taulukossa;
    - Lajiteltu taulukko rakennetaan lopusta alkaen.
'''

def counting_sort(given_array):
    if not given_array:
        return given_array

    max_value = max(given_array)
    min_value = min(given_array)
    range_of_elements = max_value - min_value + 1

    count = [0] * range_of_elements
    output = [0] * len(given_array)

    for number in given_array:
        count[number - min_value] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for number in reversed(given_array):
        count[number - min_value] -= 1
        output[count[number - min_value]] = number

    return output

if __name__ == "__main__":
    sample_array = [4, 2, 2, 8, 3, 3, 1]
    print("Original array:", sample_array)
    sorted_array = counting_sort(sample_array)
    print("Sorted array:", sorted_array)