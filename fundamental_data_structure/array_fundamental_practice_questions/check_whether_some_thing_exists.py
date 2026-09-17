def check_whether_something_exists(arr, target):
    """
    Check whether a target value exists in the given array.

    Parameters:
    arr (list): The array to search in.
    target: The value to search for.

    Returns:
    bool: True if the target exists in the array, False otherwise.
    """
    return target in arr

if __name__ == "__main__":
        arr = [10, 20, 30, 40, 50]
        target = 30
        exists = check_whether_something_exists(arr, target)
        if exists:
                print(f"{target} exists in the array.")
        else:
                print(f"{target} does not exist in the array.")
