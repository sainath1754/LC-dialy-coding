class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        for i in range(len(s)):
                stng = s[:(i+1)]
                temp= stng.count("(")-stng.count(")")
                maxi=max(maxi,temp)
        return maxi


        