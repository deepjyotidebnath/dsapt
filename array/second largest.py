def secnd(arr):
    largest=float('-inf')
    second= float('-inf')
    
    for num in arr:
        if num>largest:
            second=largest
            largest=num
        elif largest>num>second:
                second=num
    return second
                
print(secnd([10, 5, 20, 8, 15]))