def twosum(arr, target):
    left =0
    right = len(arr)-1
    
    while left< right:
        t= arr[left] + arr[right]
        
        if t ==target:
            return [left, right]
        elif t<target:
            left +=1
            
        else:
            right -=1
            
    return []
print(twosum([2,4,7,8,1],6))
        
        
        
        