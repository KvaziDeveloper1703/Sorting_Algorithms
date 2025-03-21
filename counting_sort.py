'''

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