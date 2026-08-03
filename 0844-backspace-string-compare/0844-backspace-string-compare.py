class Solution:
    def helper(self,s):
        l=[]
        for i in s:
            if i!="#":
                l.append(i)
            else:
                if len(l)!=0:
                    l.pop()
        return "".join(l)
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.helper(s)==self.helper(t)