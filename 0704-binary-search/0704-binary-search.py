class Solution:
    def search(self, a: List[int], target: int) -> int:
        l,h=0,len(a)-1
        while(l<=h):
            mid=l+(h-l)//2
            if a[mid]==target:
                return mid
            elif a[mid]<target:
                l=mid+1
            else:
                h=mid-1
        return -1
        