class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #brute force approach 
        n = len(s)
        max_len=0
        for i in range(n):
            seen=set()
            for j in range(i,n):
                ch=s[j]
                if ch in seen:break #duplicate character in set
                seen.add(ch)
                max_len= max(max_len,j-i+1)
        return max_len
