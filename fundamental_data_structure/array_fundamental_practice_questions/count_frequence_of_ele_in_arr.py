def count_frequence_of_ele_in_arr(arr, ele):
    """
    This function takes an array and an element as input and returns the frequency of that element in the array.

    :param arr: List of elements
    :param ele: Element to count frequency of
    :return: Frequency of the element in the array
    """
    count = 0
    for num in arr:
        if num == ele:
            count += 1
    return count

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    ele = 30
    print(count_frequence_of_ele_in_arr(arr, ele))