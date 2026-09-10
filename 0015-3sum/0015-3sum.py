class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result=[]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:continue  #skipping duplicates side by side
            start = i+1
            end=n-1
            while start<end:
                temp = nums[i]+nums[start]+nums[end]
                if temp==0:
                    result.append([nums[i],nums[start],nums[end]])
                    while start<end and nums[start]==nums[start+1]:
                        start+=1
                    while start<end and nums[end]==nums[end-1]:
                        end-=1
                    start+=1
                    end-=1
                elif temp<0:
                    start+=1
                else:
                    end-=1
        return result
                    
