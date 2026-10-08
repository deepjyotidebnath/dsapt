arr= [1,2 , 1, 3, 2, 1]

hashmap = {}

for num in arr:
    if num in hashmap:
        hashmap[num] += 1
        
    else:
        hashmap[num]=1
print(hashmap)