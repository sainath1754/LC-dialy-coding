class Solution:
    def condition(self,i,nums,target):
        return nums[i]>=target

    def searchInsert(self, nums: List[int], target: int) -> int:
        l,h=0,len(nums)
        while (l<h):
            mid=l+(h-l)//2
            if self.condition(mid,nums,target):
                h=mid
            else:
                l=mid+1
        return l