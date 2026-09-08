class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        in_degree = [0]*numCourses

        #building the graph
        for pair in prerequisites:
            course= pair[0]
            prereq = pair[1]
            graph[prereq].append(course)
            in_degree [course]+=1

        #courses with no requisites        
        queue = []
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        
        #how many courses we can complete will be stored in count
        count = 0 
        while queue:
            current = queue.pop(0)
            count+=1
            for neighbor in graph[current]:
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    queue.append(neighbor)
        
        # match the courses count that can be completed and numCourses 
        return count == numCourses
