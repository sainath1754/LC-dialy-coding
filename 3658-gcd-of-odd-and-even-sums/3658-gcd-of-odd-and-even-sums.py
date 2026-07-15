import math as m
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd,sumeven=0,0
        for i in range(n):
            sumodd+=((2*i) + 1)
            sumeven+= (2*(i+1))
        return m.gcd(sumeven,sumodd)