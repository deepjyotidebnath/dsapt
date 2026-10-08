def avg_subarray(arr,k):
    res= []
    window_sum=sum(arr[:k])
    res.append(window_sum/k)
    for i in range(k, len(arr)):
        window_sum +=arr[i]- arr[i-k]
        res.append(window_sum/k)
    return res
print(avg_subarray([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))