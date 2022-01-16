tc = int(input())

for i in range(tc):
    num = int(input())   ######## 4원을 만들어야된다

    cost = list(map(int, input().split())) #####3 1 2 3  3개의 숫자: 1 2 3
    cost = [0] + cost[1:]   ##### 0 1 2 3  :  0원 1원 2원 3원을 이용한다
    v = [[0 for i in range(num+1)] for j in range(len(cost))]
    v[0][0] = 1
    for i in range(0, num+1):
        v[1][i] = 1
    for i in range(2, len(cost)):
        for j in range(0, num+1):
            if j < cost[i]:
                v[i][j] = v[i-1][j]
            if cost[i] <= j:
                v[i][j] = v[i][j-cost[i]] + v[i-1][j]

    print(v[len(cost)-1][num])