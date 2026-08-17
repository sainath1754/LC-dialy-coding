class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count,left,maxi={},0,0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right], 0) + 1
            while (count[s[right]]>2):
                count[s[left]]-=1
                left+=1
            maxi=max(maxi,right-left+1)
        return maxi