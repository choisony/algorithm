n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
parent[1] = 99999
visited = [False] * (n + 1)
cycle = False
cycle_num = [0,0]


def dfs(start):
    global cycle
    global cycle_num
    if visited[start] == False:
        visited[start] = True
        for i in graph[start]:
            if parent[i] ==0:
                parent[i] = start
                dfs(i)
            elif visited[i] == True and parent[start] != i and i  !=1 and parent[start] !=1:
                cycle = True
                cycle_num = [start, i]
                
dfs(1)

ans = []
cycle_num.sort(reverse= True)
idx = cycle_num[0]
ans.append(idx)
while(1):
    ans.append(parent[idx])
    idx = parent[idx]
    if idx == cycle_num[1]:
        break


ans.sort()
print(len(ans))
print(ans)
