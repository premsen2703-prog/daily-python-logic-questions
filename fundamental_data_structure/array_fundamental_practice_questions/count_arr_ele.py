def count_arr_ele(arr):
    """
    This function takes an array as input and returns the count of its elements.

    :param arr: List of elements
    :return: Count of the elements in the array
    """
    count = 0
    for _ in arr:
        count += 1
    return count

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print(count_arr_ele(arr))
    
