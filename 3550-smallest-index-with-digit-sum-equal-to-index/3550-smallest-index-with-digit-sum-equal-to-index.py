class Solution:
    def summ(self,n):
        temp=0
        while(n>0):
            temp+=n%10
            n//=10
        return temp
    def smallestIndex(self, nums: List[int]) -> int:
        mini=-1
        flag=True
        for i in range(len(nums)):
            print(i,self.summ(nums[i]))
            if i==self.summ(nums[i]):
                if flag:
                    mini=i
                    flag=False
                else:
                    mini=min(mini,i)
        return mini

        