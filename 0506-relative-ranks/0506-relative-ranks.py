class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d={}
        s = sorted(score,reverse=True)
        result = []
        for i in range(len(s)):
            if i==0:d[s[i]]="Gold Medal"
            elif i==1:d[s[i]]="Silver Medal"
            elif i==2:d[s[i]]="Bronze Medal"
            else:d[s[i]]= str(i+1)
        for j in score:
            result.append(d[j])
        return result



        