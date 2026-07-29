class Solution:
    def smallestPalindrome(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        odd_length=""
        flag=False
        for i in d:
            if d[i]%2!=0:
                odd_length = i
                flag=True
        result = ""
        for i in sorted(d.keys()):
            result+= (i*(d[i]//2))
        if flag:
            return result+odd_length+result[::-1]
        else:
            return result+result[::-1]
        