class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        answer = ""
        l = sorted(d.items(), key=lambda x: x[1], reverse=True)
        for i in l:
            answer+=i[0]*i[1]
        return answer

        