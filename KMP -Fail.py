def getFail(pattern):
    fail =[0]*len(pattern)
    j=0
    for i in range(1,len(pattern)):
        while(j>0 and (pattern[i] != pattern[j])):
            j = fail[j-1]
        if pattern[i] == pattern[j]:
            j+=1
            fail[i] +=j
        else:
            fail[i] = j;
    return fail

def kmp_count(text,pattern,fail):
    answer=0
    j=0
    for i in range(len(text)):
        while(j>0 and text[i] != pattern[j]):
            j = fail[j-1]
        if pattern[j] == text[i]:
            if j==len(pattern)-1:
                answer+=1
                j= fail[j]
            else:
                j+=1
    return answer


tc = int(input())
for _ in range(tc):
    pattern, text = map(str,input().split())
    pattern,text = list(pattern), list(text)
    fail= getFail(pattern)
    answer= kmp_count(text,pattern,fail)
    for i in fail:
        print(i,end=' ')
    print()
    print(answer)
