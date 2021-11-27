# import sys
# import heapq
# INF=int(1e9)
# max_num = INF
#
# tc = int(sys.stdin.readline())
# for _ in range(tc):
#     n = int(sys.stdin.readline())
#     g = {}
#     graph= [[0]*(n+1) for _ in range(n+1)]
#     for i in range(n):
#         l = list(map(int,sys.stdin.readline().split()))
#         edge_count = l[1]
#         if edge_count >0:
#             for j in range(2,len(l),2):
#                 graph[l[0]][l[j]] = l[j+1]
#                 if l[0] not in g.keys():
#                     g[l[0]] = [l[j]]
#                 else:
#                     g[l[0]].append(l[j])
#
#     ##### g : key노드는 value 노드에 연결되어있다는걸 보여줌
#     ##### {1: [2, 3], 2: [5, 6], 3: [7, 8], 4: [1, 3], 5: [3, 6], 6: [9, 10], 7: [5, 6, 8, 9], 8: [4, 9], 9: [10]}
#     dp= [max_num]*(n+1)        ####### i 번째 노드까지의 거리 ,노드가 10개면 11개 배열들어서 1,2,3,4,~~ 8,9,10까지 할당하게끔
#     dist = [max_num] * (n+1)   ####### i 번째 노드와 그 이전노드 사이의 거리 (이 값들을 더해서 답이 나옴)
#     dp[1]= 0
#     hq = []
#     heapq.heappush(hq,[0,1])      ########(거리 , i번째노드까지)
#
#     while len(hq)!=0:
#         weight,city = heapq.heappop(hq)
#         if dp[city]  <weight:
#             continue
#         if city in g:
#             for i in g[city]:
#                 weight2= graph[city][i]+weight
#                 if weight2 < dp[i]:
#                     dp[i] = weight2
#                     heapq.heappush(hq,[weight2,i])
#                     dist[i] = graph[city][i]
#     answer= 0
#     for f in dist[2:]:
#         if f != max_num:
#             answer +=f
#     print(answer)

###############################################################answer
########set이용###################
import sys
from queue import PriorityQueue
max_num = int(1e9)

tc = int(sys.stdin.readline())
for _ in range(tc):
    n = int(sys.stdin.readline())
    s = {}
    graph= [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        i_list = list(map(int,sys.stdin.readline().split()))
        edge_count = i_list[1]
        if edge_count >0:
            for j in range(2,len(i_list),2):
                graph[i_list[0]][i_list[j]] = i_list[j+1]
                if i_list[0] not in s.keys():
                    s[i_list[0]] = [i_list[j]]
                else:
                    s[i_list[0]].append(i_list[j])

    dp= [max_num]*(n+1)
    dist = [max_num] * (n+1)
    dp[1]= 0
    p = PriorityQueue()
    p.put([0,1])
    parent = [0] * (n+1)
    set_n = set()
    while not p.empty():
        weight,city = p.get()
        if dp[city]  <weight:
            continue
        if city in s:
            for i in s[city]:
                weight2= graph[city][i]+weight
                if weight2 < dp[i]:
                    dp[i] = weight2
                    p.put([weight2,i])
                    parent[i] = city
                    dist[i] = graph[city][i]

    for k in range(2,n+1):
        a=parent[k]
        set_n.add((a,k))
        while a !=1:
            temp =parent[a]
            set_n.add((temp,a))
            a= temp
    sum = 0
    for u,v in set_n:
        sum +=  graph[u][v]
    print(sum)

