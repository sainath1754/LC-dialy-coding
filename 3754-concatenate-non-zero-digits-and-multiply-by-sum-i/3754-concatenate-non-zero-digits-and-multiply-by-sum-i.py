class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:return 0
        total = 0
        value= ""
        while (n>0):
            temp=n%10
            if temp!=0:
                value=str(temp)+value
            total+=temp
            n=n//10
        return int(value)*total
        
        