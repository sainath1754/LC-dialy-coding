class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b,a,l,o,n=0,0,0,0,0
        for i in text:
            if i=='b':b+=1
            elif i=='a':a+=1
            elif i=='l':l+=1
            elif i=='o':o+=1
            elif i=='n':n+=1
        mini1 = min(b,a,n)
        mini2=min(l//2,o//2)
        if mini1 <= mini2:return mini1
        else:return mini2

             
        