class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:return 0
        if len(nums)==1:return nums[0]
        def money(houses):
            m=len(houses)
            if m==0:return 0
            if m==1:return houses[0]
            dp=[0]*(m+1)
            dp[1]=houses[0]
            for i in range(2,m+1):
                dp[i]=max(dp[i-1],dp[i-2]+houses[i-1])
            return dp[m]
        case1=money(nums[:-1])
        case2=money(nums[1:])
        return max(case1,case2)
        