class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp=target-nums[i]
            if (temp in nums) and (nums.index(temp)!=i):
                return [i,nums.index(temp)]
 
