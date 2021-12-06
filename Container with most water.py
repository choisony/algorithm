def maxArea(height):
    i=0
    j = len(height)-1
    result=-9999999
    while(i!=j):
        if i==j:
            break
        if height[i] <=height[j]:
            result = max(result,height[i]*(j-i))
            i+=1
        else:
            result = max(result,(height[j]*(j-i)))
            j-=1
    return result
print(maxArea([2,3,4,5,18,17,6]))

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

# Example 2:
# Input: height = [1,1]
# Output: 1

# Example 3:
# Input: height = [4,3,2,1,4]
# Output: 16

# Example 4:
# Input: height = [1,2,1]
# Output: 2
