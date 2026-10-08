# queue=[]
# queue.append(10)
# queue.append(20)
# queue.append(30)

# print(queue)
from collections import deque
queue = deque([1, 2, 3, 4, 5])

stack=[]
while queue:
    stack.append(queue.popleft())
while stack:
    queue.append(stack.pop())
print(queue)