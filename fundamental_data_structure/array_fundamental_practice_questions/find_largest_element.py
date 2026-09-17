def largest_element(arr):
    if not arr:
        return None
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

if __name__=="__main__":

    arr = [10,20,30,40,50]

    print(largest_element(arr))

