def linear(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
        
    return "None"
print(linear([2,3,6,3,8],3))