def sum_of_array_elements(arr):
    """
    This function takes an array as input and returns the sum of its elements.

    :param arr: List of numbers
    :return: Sum of the elements in the array
    """
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print(sum_of_array_elements(arr))