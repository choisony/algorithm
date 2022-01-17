import sys
from queue import PriorityQueue

N= 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K =3
for case in range(N):
    dist = [500000] * (N + 1)
    dist[case+1] = 0
    q = PriorityQueue()
    q.put([0, case+1])  ##########[거리 , N까지의]

    while not q.empty():
        weight, position = q.get()
        if weight > dist[position]:
            continue

        for i in range(len(road)):
            if road[i][0] == position:
                weight2, there = road[i][2] + weight, road[i][1]
                if weight2 < dist[there]:
                    dist[there] = weight2
                    q.put([weight2, there])
            elif road[i][1] == position:
                weight2, there = road[i][2] + weight, road[i][0]
                if weight2 < dist[there]:
                    dist[there] = weight2
                    q.put([weight2, there])

    # answer = 0
    # for i in dist:
    #     if i<=K:
    #         answer+=1
    print(case+1 ,"'s shortest path  :",dist[1:])




