class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # #brute force approach 
        # n = len(s)
        # max_len=0
        # for i in range(n):
        #     seen=set()
        #     for j in range(i,n):
        #         ch=s[j]
        #         if ch in seen:break #duplicate character in set
        #         seen.add(ch)
        #         max_len= max(max_len,j-i+1)
        # return max_len

        #optimized approch
        dict = {}
        left=0
        max_len=0
        n=len(s)
        for right in range(n):
            if s[right] in dict: #duplicate existed
                left=max(left , dict[s[right]]+1) 
                #abcdefeg   left will be moved to f (index=5)
                #left is moved till the charcters next index
            dict[s[right]]=right # new iteration right start point
            max_len =max(max_len,right-left+1)
        return max_len