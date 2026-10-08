def selection(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if arr[j]< arr[min_i]:
                min_i=j
        arr[i], arr[min_i]=arr[min_i], arr[i]
    return arr
print(selection([67,90,56,34, 54, 21]))
                