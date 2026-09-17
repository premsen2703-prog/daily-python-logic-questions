def search(arr, target):
    n= len(arr)
    for i in range(0, n):
        if (arr[i] == target):
            return i
    return -1
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target = 3
    result = search(arr, target)
    if result !=  -1:
        print(f"Element found at index:{result}")
    else:
        print("Element not found  in index",result)
