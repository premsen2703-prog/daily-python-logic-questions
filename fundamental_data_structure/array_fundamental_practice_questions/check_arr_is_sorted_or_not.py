def check_arr_is_sorted(arr):
    """
    Check whether the given array is sorted in non-decreasing order.

    Parameters:
    arr (list): The array to check.

    Returns:
    bool: True if the array is sorted, False otherwise.
    """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    is_sorted = check_arr_is_sorted(arr)
    if is_sorted:
        print("The array is sorted.")
    else:
        print("The array is not sorted.")
        
