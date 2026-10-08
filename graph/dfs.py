graph={
    0:[1,2],
    1:[3],
    2:[4],
    3:[],
    4:[]
}
visited = set()
def dfs(node):
    if node in visited:
        return
    visited.add(node)
    print(node, end=" ")
    for neighbour in graph[node]:
        dfs(neighbour)
dfs(0)
