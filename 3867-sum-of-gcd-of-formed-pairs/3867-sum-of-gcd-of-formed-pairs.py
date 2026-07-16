import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixgcd = []
        curr=nums[0]
        for i in nums:
            curr = max(curr,i)
            val = math.gcd(i,curr)
            prefixgcd.append(val)
        prefixgcd.sort()
        total = 0
        n=len(nums)
        j,k=0,n-1
        while (j<k):
            total = total + math.gcd(prefixgcd[j],prefixgcd[k])
            #print(total)
            j+=1
            k-=1
        return total
        