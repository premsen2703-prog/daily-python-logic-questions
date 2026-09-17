def binary_search(arr,x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
if __name__=="__main__":
    arr = [90,30,20,40,70,60,50,80,10,100]
    x = int(input("Enter the element to be searched:"))
    result = binary_search(arr,x)
    if result != -1:
        print(f"Element found at index:{result}")
    else:
        print("Element not found in index",result)