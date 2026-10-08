arr =[1, 3, 4,5,8,2,1]
seen = set()
for num in arr:
    if num in seen:
        print("Duplicate",num)
        break
    seen.add(num)