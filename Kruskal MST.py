# 1
# 10
# 1 3 2 9 3 8 4 5
# 2 3 1 9 5 7 6 9
# 3 5 1 8 4 3 5 2 7 3 8 5
# 4 3 1 5 3 3 8 7
# 5 4 2 7 3 2 6 5 7 4
# 6 5 2 9 5 5 7 6 9 9 10 8
# 7 5 3 3 5 4 6 6 8 4 9 7
# 8 4 3 5 4 7 7 4 9 4
# 9 4 6 9 7 7 8 4 10 3
# 10 2 6 8 9 3

def find_set(x):
    while x!= root[x]:
        x= root[x]
    return x

import sys
import heapq
tc = int(sys.stdin.readline())
for _ in range(tc):
    n = int(sys.stdin.readline())
    # set_node = [set([i]) for i in range(n+1)]
    g = {}
    hq= []
    graph= [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        l = list(map(int,sys.stdin.readline().split()))
        edge_count = l[1]
        if edge_count >0:
            for j in range(2,len(l),2):
                graph[l[0]][l[j]] = l[j+1]
                heapq.heappush(hq,(l[j+1],(l[0],l[j])))

    answer= 0
    first = heapq.heappop(hq)
    answer+= first[0]
    a,b = first[1]
    root = [i for i in range(n+1)]
    root[b] = a
    node= 1
    while hq:
        q = heapq.heappop(hq)
        x,y = q[1]
        if find_set(x) != find_set(y):
            answer+=q[0]
            root[find_set(y)] = find_set(x)
            node+=1
        if node >=n-1:
            break
    print(answer)


