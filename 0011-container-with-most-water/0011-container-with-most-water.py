class Solution:
    def maxArea(self, l: List[int]) -> int:
        i=0
        j=len(l)-1
        maxi=0
        while(i<j):
            curr = min(l[i],l[j])*(j-i)
            if l[i]<=l[j]:
                i+=1
            else:
                j-=1
            maxi=max(maxi,curr)
        return maxi
