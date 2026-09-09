class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid) #rows
        n = len(grid[0])#columns
        if not grid:
            return 0
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]#up, down,left,right
        def bfs(r,c):
            """
            we will make the islands as 0's and so in next iteration 
            they wont be found again
            """
            queue=[(r,c)]
            grid[r][c]='0'
            while queue:
                x,y=queue.pop(0)
                for dx,dy in dirs:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]=="1":
                        grid[nx][ny]='0'
                        queue.append((nx,ny))
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    count+=1
                    bfs(i,j)
        return count

        