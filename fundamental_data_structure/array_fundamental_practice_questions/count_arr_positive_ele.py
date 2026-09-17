def arr_positive_ele(arr):
    """
    This function takes an array as input and returns the count of positive elements in it.

    :param arr: List of elements
    :return: Count of positive elements in the array
    """
    count = 0
    for num in arr:
        if num > 0:
            count += 1
    return count

if __name__ == "__main__":
    arr = [10, -20, 30, -40, 50]
    print(arr_positive_ele(arr))