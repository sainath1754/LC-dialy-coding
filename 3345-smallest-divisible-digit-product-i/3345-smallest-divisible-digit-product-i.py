class Solution:
    def helper(self,v):
        val = str(v)
        temp=1
        for j in val:
            temp*=int(j)
        return temp

    def smallestNumber(self, n: int, t: int) -> int:
        flag=True
        while flag:
            if self.helper(n)%t==0:
                flag=False
                return n
            n+=1
        