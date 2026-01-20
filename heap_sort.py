'''
Heap Sort is an efficient sorting algorithm based on the binary heap data structure. The algorithm builds a max-heap from the array, then repeatedly extracts the largest element (the root of the heap) and places it at the end of the array.

How the algorithm works:
    - The array is transformed into a max-heap, where each parent is greater than its children;
    - The largest element (root) is swapped with the last element in the array;
    - The heap size is reduced, and the heapify function is called to restore the heap property;
    - This process repeats until the array is fully sorted.

Сортировка кучей - это эффективный алгоритм сортировки, основанный на структуре данных бинарная куча (binary heap). Алгоритм строит максимальную кучу из массива, а затем поочерёдно извлекает наибольший элемент (корень кучи), помещая его в конец массива.

Как работает алгоритм:
    - Массив преобразуется в max-heap, где каждый родительский элемент больше своих дочерних;
    - Затем самый большой элемент (в корне) меняется местами с последним элементом массива;
    - Размер кучи уменьшается, и для нового корня вызывается функция heapify, восстанавливающая свойства кучи;
    - Повторяется, пока массив не будет отсортирован.

Keanolajittelu (heap sort) on tehokas lajittelualgoritmi, joka perustuu binääriseen kekoon (binary heap) -tietorakenteeseen. Algoritmi muodostaa taulukosta maksimikeon (max-heap) ja sen jälkeen poistaa vuorotellen suurimman alkion (keon juuren), siirtäen sen taulukon loppuun.

Miten algoritmi toimii:
    - Taulukko muunnetaan max-heap-rakenteeksi, jossa jokainen vanhempi alkio on suurempi kuin sen lapsialkiot;
    - Sen jälkeen suurin alkio (juuressa) vaihdetaan taulukon viimeisen alkion kanssa;
    - Keon koko pienenee, ja uudelle juurelle kutsutaan heapify-funktio, joka palauttaa keon ominaisuudet;
    - Prosessia toistetaan, kunnes taulukko on kokonaan lajiteltu.
'''

def heapify(given_array, N, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < N and given_array[left] > given_array[largest]:
        largest = left

    if right < N and given_array[right] > given_array[largest]:
        largest = right

    if largest != i:
        given_array[i], given_array[largest] = given_array[largest], given_array[i]
        heapify(given_array, N, largest)

def heap_sort(given_array):
    N = len(given_array)

    for i in range(N // 2 - 1, -1, -1):
        heapify(given_array, N, i)

    for i in range(N - 1, 0, -1):
        given_array[i], given_array[0] = given_array[0], given_array[i]
        heapify(given_array, i, 0)

    return given_array

if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", sample_array)
    sorted_array = heap_sort(sample_array)
    print("Sorted array:", sorted_array)