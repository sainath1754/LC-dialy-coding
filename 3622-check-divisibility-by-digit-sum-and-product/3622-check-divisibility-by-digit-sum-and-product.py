class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total, multi = 0,1
        value=n
        while (n>0):
            temp=n%10
            n//=10
            total+=temp
            multi*=temp
        print(total,multi)
        return value%(total+multi)==0
        