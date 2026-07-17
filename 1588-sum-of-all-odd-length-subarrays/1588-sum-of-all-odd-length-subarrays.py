class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        n = len(arr)
        for i in range(n+1):
            for j in range(i+1,n+1):
                val = arr[i:j]
                if len(val)%2!=0:
                    result+=sum(val)
        return result
        