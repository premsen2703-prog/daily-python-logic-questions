def duplicate_elements(arr):
    # This function takes an array as input and returns the first duplicate element found in it.
    # :param arr: List of elements
    # :return: The first duplicate element in the array, or None if no duplicates are found.
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)