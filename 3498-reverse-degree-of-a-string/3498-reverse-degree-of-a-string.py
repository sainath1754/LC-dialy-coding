class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            idx_val=ord('a')-ord(s[i])+26
            result+=(idx_val*(i+1))
            print(idx_val)
        return result
        