class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n):
            freq = 0
            for j in range(i, n):
                if nums[j] == target:freq += 1
                if 2 * freq > j - i + 1:cnt += 1
        return cnt
