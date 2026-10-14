class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        flag=True
        i=1
        while flag:
            if k*i not in nums:
                flag=False
                return k*i
            i+=1


        