import sys
import heapq
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
INF=int(1e9)
max_num = INF

tc = int(sys.stdin.readline())
for _ in range(tc):
    n = int(sys.stdin.readline())
    g = {}
    q= []
    graph= [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        l = list(map(int,sys.stdin.readline().split()))
        edge_count = l[1]
        if edge_count >0:
            for j in range(2,len(l),2):
                graph[l[0]][l[j]] = l[j+1]
                if l[0] not in g.keys():
                    g[l[0]] = [l[j]]
                else:
                    g[l[0]].append(l[j])


    key= [max_num]*(n+1)        ####### i 번째 노드까지의 거리 ,노드가 10개면 11개 배열들어서 1,2,3,4,~~ 8,9,10까지 할당하게끔
    dist = [max_num] * (n+1)   ####### i 번째 노드와 그 이전노드 사이의 거리 (이 값들을 더해서 답이 나옴)
    visited = [0] * (n+1)
    visited[1] = 1
    key[1]= 0
    heapq.heappush(q,[0,1])
    while(q):
        # print(q)
        weight ,node = heapq.heappop(q)
        # print("weight: ",weight,"node: ",node)
        for i in g[node]:
            if visited[i] != 1 and graph[node][i] < key[i]:
                dist[i] = graph[node][i]
                key[i] = dist[i]
                heapq.heappush(q,[dist[i],i])
        visited[node]=1

    answer = 0

    for i in dist[2:]:
        answer+=i
    print(answer)

