from collections import deque
def binary(n):
    q=deque()
    q.append("1")
    
    for _ in range(n):
        front = q.popleft()
        print(front)
        q.append(front +"0")
        q.append(front+"1")
        
print(binary(5))