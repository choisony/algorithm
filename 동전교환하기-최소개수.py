# import sys
#
# tc = int(input())
# for i in range(tc):
#     won = int(input())
#     won2 = won
#     won_list = list(map(int,input().split()))[1:]
#     ans = 0
#     for i in range(len(won_list)-1,-1,-1):
#         ans += won //won_list[i]
#         won %=  won_list[i]
#
#     for i in won_list:
#         if won2%i==0 and i!=1:
#             ans = min(ans,won2//i)
#     print(ans)

# import sys
#
tc = int(input())
for i in range(tc):
    won = int(input())
    coin = list(map(int,input().split()))[1:]
    dp=[0]
    dp2 = [9999999999 for i in range(0,won)]
    dp = dp+dp2
    for i in range(0,len(coin)):
        for j in range(coin[i],won+1):
            dp[j] = min(dp[j], dp[j - coin[i]] + 1)

    print(dp[won])
