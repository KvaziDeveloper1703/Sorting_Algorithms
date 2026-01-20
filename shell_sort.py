'''
Shell Sort is an optimized version of insertion sort that allows elements far apart from each other to be compared and moved. The algorithm uses a sequence of gaps, which gradually decreases to 1. In each step, insertion sort is performed on sublists formed by elements that are gap distance apart.

How the algorithm works:
    - The initial gap is set to half the length of the array;
    - Perform insertion sort on elements at each gap distance;
    - After each pass, reduce the gap by half until it reaches 0.

Сортировка Шелла - это улучшенная версия сортировки вставками, которая позволяет сравнивать и перемещать элементы, находящиеся далеко друг от друга. Алгоритм использует последовательность промежутков, которая постепенно уменьшается до 1. На каждом шаге выполняется сортировка подсписков, состоящих из элементов, отстоящих друг от друга на текущий gap.

Как работает алгоритм:
    - Начальный шаг равен половине длины массива;
    - Выполняется сортировка вставками для элементов, находящихся на расстоянии gap;
    - После каждой итерации gap уменьшается вдвое, пока не достигнет 0.

Shell-lajittelu (Shell sort) on parannettu versio lisäyslajittelusta, joka mahdollistaa kaukana toisistaan olevien alkioiden vertailun ja siirtämisen. Algoritmi käyttää askelväliä (gap), joka pienenee vähitellen arvoon 1. Jokaisessa vaiheessa suoritetaan lisäyslajittelu alijonoille, joissa alkiot ovat toisistaan nykyisen gapin verran.

Miten algoritmi toimii:
    - Alkuväli on puolet taulukon pituudesta;
    - Suoritetaan lisäyslajittelu alkioille, jotka ovat gap-etäisyydellä toisistaan;
    - Jokaisen kierroksen jälkeen gap pienennetään puoleen, kunnes se saavuttaa arvon 0.
'''

def shell_sort(given_array):
    N = len(given_array)
    gap = N // 2

    while gap > 0:
        for i in range(gap, N):
            temporary = given_array[i]
            j = i
            while j >= gap and given_array[j - gap] > temporary:
                given_array[j] = given_array[j - gap]
                j -= gap
            given_array[j] = temporary
        gap //= 2

    return given_array

if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", sample_array)
    sorted_array = shell_sort(sample_array)
    print("Sorted array:", sorted_array)