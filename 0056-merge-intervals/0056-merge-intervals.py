class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        #soring intervals based on first element
        result=[]
        for i in intervals:
            start,end=i[0],i[1]
            if not result:result.append(i)
            else:
                #if there is a merge
                last_start=result[-1][0]
                last_end=result[-1][1]
                if start<=last_end: 
                    #what is the big end point of intervals merged
                    new_end=max(last_end,end)
                    result[-1][1]=new_end
                else:
                    #if there is a no merge
                    result.append(i)
        return result
        