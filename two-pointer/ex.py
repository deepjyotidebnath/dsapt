def remove(arr):
    x= sorted(arr)
    y=set(x)
    ans=len(x)- len(y)
    return ans
print(remove([0,0,1,1,1,2,2,3,3,4]))


