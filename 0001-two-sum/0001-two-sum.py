class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}#d={}
        for i in range(len(nums)): #i=1 nums[i]=3
            temp=target-nums[i]#temp=6-3=3
            if temp in d: #3 in d
                return [d[temp],i] # d[temp] -> value  2 's value and present i value
            d[nums[i]]=i #d[3]=0   in dict : key-list lo value, value - index
        return []