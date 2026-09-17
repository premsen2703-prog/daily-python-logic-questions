def first_occurrence(arr, target):
    """
    Function to find the first occurrence of a target element in an array.
    
    Parameters:
    arr (list): The input array.
    target: The element to find the first occurrence of.
    
    Returns:
    int: The index of the first occurrence of the target element, or -1 if not found.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 20]
    target = 20
    result = first_occurrence(arr, target)
    if result != -1:
        print(f"The first occurrence of {target} is at index: {result}")
    else:
        print(f"{target} not found in the array.")