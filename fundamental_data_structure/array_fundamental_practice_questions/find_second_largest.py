def second_largest(arr):
    if len(arr) < 2:
        return None
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return None if second == float('-inf') else second

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print(second_largest(arr))