class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        maxi = len(str(high))
        s ='123456789'
        l=[]
        for i in range(len(s)+1):
            for j in range(i+1,len(s)+1):
                value = int(s[i:j])
                if value>=low and value<=high:
                    l.append(value)
        l.sort()
        return l