stack = [10, 20, 30,40, 50]

value = 30
found = False
while stack:
    element = stack.pop()
    if element==value:
        found=True
if found:
    print("true")
else:
    print("not found")