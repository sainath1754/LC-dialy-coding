class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""
        l = []
        for i in s:
            if len(l)>=2 and l[-1]==i and l[-2]==i:
                continue
            else:
                l.append(i)
        print(l)
        for i in l:
            result+=i
        return result
