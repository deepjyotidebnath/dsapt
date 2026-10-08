stack =[]
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack", stack)
item= stack.pop()
print("Popped:", item)

print("Top:", stack[-1])

print("Is Empty:", len(stack)==0)