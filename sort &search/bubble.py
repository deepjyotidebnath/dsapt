def bubble(arr):
    n= len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
    return arr
print(bubble([9,5,1,10,3,6,1]))