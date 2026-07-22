class Solution:
    def sortVowels(self, s: str) -> str:
        temp,result=[],""
        for i in s:
            if i in 'AEIOUaeiou':
                temp.append(i)
        temp.sort()
        pos=0
        for i in s:
            if i not in 'AEIOUaeiou':
                result+=i
            else:
                result+=temp[pos]
                pos+=1
        return result
        
        