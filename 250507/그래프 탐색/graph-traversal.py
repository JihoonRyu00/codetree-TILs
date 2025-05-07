n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
visit=[False]*(n+1)

edge_list={i:[] for i in range(1,n+1)}
for edge in edges:
    edge_list[edge[0]].append(edge[1])
    edge_list[edge[1]].append(edge[0])

visit[1]=True
def dfs(node):
    count=1
    next_nodes=edge_list[node]
    for next_node in next_nodes:
        if not visit[next_node]:
            visit[next_node]=True
            count+=dfs(next_node)
    return count

print(dfs(1)-1)
