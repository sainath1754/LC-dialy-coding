class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        d={'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','g':'6','h':'7','i':'8','j':'9'}
        v1,v2,v3="","",""
        for i in firstWord:
            v1+=d[i]
        for i in secondWord:
            v2+=d[i]
        for i in targetWord:
            v3+=d[i]
        return (int(v1)+int(v2) == int(v3))
        
        