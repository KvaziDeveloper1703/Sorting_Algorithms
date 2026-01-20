'''
Bucket Sort is an efficient sorting algorithm for floating-point numbers that are uniformly distributed across a range. It divides the array into multiple subgroups, sorts each bucket individually (commonly with insertion sort), and then concatenates the results.

How the algorithm works:
    - Determine the minimum and maximum values of the array;
    - The array is split into num_buckets buckets, each representing a specific range;
    - Elements are distributed into buckets based on their value;
    - Each bucket is sorted using insertion sort;
    - All sorted buckets are concatenated into the final sorted array.

Сортировка по корзинам - это эффективный алгоритм для сортировки вещественных чисел, равномерно распределённых по диапазону. Он делит массив на несколько подмножеств, сортирует каждую корзину отдельно (обычно сортировкой вставками) и затем объединяет результат.

Как работает алгоритм:
    - Находятся минимальное и максимальное значения массива;
    - Массив делится на num_buckets корзин, каждая из которых охватывает определённый диапазон значений;
    - Элементы распределяются по корзинам на основе их значения;
    - Каждая корзина сортируется с помощью сортировки вставками;
    - Все отсортированные корзины объединяются в итоговый массив.

Korilajittelu (bucket sort) on tehokas lajittelualgoritmi reaalilukujen lajitteluun, kun luvut ovat jakautuneet tasaisesti tietylle välille. Algoritmi jakaa taulukon useisiin alijoukkoihin (koreihin), lajittelee jokaisen korin erikseen (yleensä lisäyslajittelulla) ja yhdistää lopuksi tulokset.

Miten algoritmi toimii:
    - Etsitään taulukon pienin ja suurin arvo;
    - Taulukko jaetaan num_buckets koriin, joista jokainen kattaa tietyn arvoalueen;
    - Alkiot jaetaan koreihin niiden arvon perusteella;
    - Jokainen kori lajitellaan lisäyslajittelulla;
    - Kaikki lajitellut korit yhdistetään lopulliseksi taulukoksi.
'''

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

def bucket_sort(given_array):
    if not given_array:
        return given_array

    number_of_buckets = len(given_array)
    max_value = max(given_array)
    min_value = min(given_array)
    bucket_range = (max_value - min_value) / number_of_buckets + 1e-9

    buckets = [[] for _ in range(number_of_buckets)]

    for number in given_array:
        index = int((number - min_value) / bucket_range)
        buckets[index].append(number)

    sorted_array = []
    
    for bucket in buckets:
        sorted_array.extend(insertion_sort(bucket))

    return sorted_array

if __name__ == "__main__":
    sample_array = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
    print("Original array:", sample_array)
    sorted_array = bucket_sort(sample_array)
    print("Sorted array:", sorted_array)