def second_smallest(arr):
    if len(arr) < 2:
        return None
    smallest = second = float('inf')
    for num in arr:
        if num < smallest:
            second = smallest
            smallest = num
        elif num < second and num != smallest:
            second = num
    return None if second == float('inf') else second

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print(second_smallest(arr))