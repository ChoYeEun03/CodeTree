n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[False]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

for a,b in edges:
    graph[a][b] = True
    graph[b][a]=True

def dfs(vertex):
    for curr_v in range(1, n+1):
        if graph[vertex][curr_v] and not visited[curr_v]:
            visited[curr_v] = True
            dfs(curr_v)

visited[1]=True
dfs(1)
print(sum(visited)-1)

