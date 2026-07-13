class Solution:
    def search(self,l: List[int], target: int) -> int:
        low=0
        high=len(l)-1
        while(low<=high):
            mid=high - ((high-low)//2)
            if l[mid]==target:return mid
            elif l[mid]>target:high=mid-1
            else:low=mid+1
        return -1
        