class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        l=[]
        for i in word:
            if i.lower()==i and i not in l:
                l.append(i)
        cnt=0
        for i in l:
            if i.upper() in word:
                cnt+=1
        return cnt
        