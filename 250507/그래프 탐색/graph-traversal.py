n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
visit=[False]*(n+1)

edge_list={i:[] for i in range(1,n+1)}
for edge in edges:
    if edge[0] in edge_list:
        edge_list[edge[0]].append(edge[1])
    else:
        edge_list[edge[0]]=[edge[1]]
    if edge[1] in edge_list:
        edge_list[edge[1]].append(edge[0])
    else:
        edge_list[edge[1]]=[edge[0]]

visit[1]=True
def bfs(node):
    count=1
    next_nodes=edge_list[node]
    for next_node in next_nodes:
        if not visit[next_node]:
            visit[next_node]=True
            count+=bfs(next_node)
    return count

print(bfs(1)-1)