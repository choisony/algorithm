# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]

tc = int(input())
for _ in range(tc):
    pattern, text = map(str,input().split())
    pattern,text = list(pattern), list(text)
    dfa = [[0] * (len(pattern)+1) for i in range(4)]
    for i in range(len(pattern)):
        if pattern[i]=="A":
            pattern[i] =0
        if pattern[i]=="B":
            pattern[i] =1
        if pattern[i]=="C":
            pattern[i] =2
    for i in range(len(text)):
        if text[i]=="A":
            text[i] =0
        if text[i]=="B":
            text[i] =1
        if text[i]=="C":
            text[i] =2
    dfa[pattern[0]][0]=1
    x=0
    for j in range(1,len(pattern)+1):
        for c in range(4):
            dfa[c][j] = dfa[c][x]
        if j<len(pattern):
            dfa[pattern[j]][j] = j+1
            x= dfa[pattern[j]][x]

    i=0
    j=0
    answer=0
    while(i<len(text) or j<len(pattern)):
        # print("index: ",i,"j: ",j)
        if i==len(text):
            break
        j= dfa[text[i]][j]
        if j==len(pattern):
            answer+=1
        i+=1
    count=0
    for i in range(4):
        for j in range(len(dfa[0])):
            if dfa[i][j] !=0:
                count+=1
    print(count,answer)