def minimum_ele(arr):
    min = arr[0]
    for i in arr:
        if i < min :
            mni = i
    return min

if __name__=="__main__":
    arr = [10,20,30,40,50]

    print(minimum_ele(arr))