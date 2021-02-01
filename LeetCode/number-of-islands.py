'''
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

'''

'''
Given an m x n 2d grid map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume all
four edges of the grid are all surrounded by water.
'''

'''
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

'''
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

'''


class ShubhamGraph:
    def __init__(self,row, col,gp):
        self.row1=row
        self.col1=col
        self.gr=gp
    def checksafe(self,i,j,visited):
        return (i>=0 and i< self.row1 and j<self.col1 and j>=0 and not visited[i][j] and self.gr[i][j])
    def h1(self,i,j,visited):

        visited[i][j]=True
        row_neighbour=[-1,-1,0,0,1,1]
        col_neighbour=[0,1,-1,1,-1,0]
        for k in range(6):
            if self.checksafe(i+row_neighbour[k],j+col_neighbour[k],visited):
                self.h1(i+row_neighbour[k],j+col_neighbour[k],visited)




    def countiland(self):
        visited=[[False for j in range(self.col1)]for i in range (self.row1)]
        #count for island is c
        c=0
        for i in range(self.row1):
            for j in range(self.col1):
                if visited [i][j]==False and self.gr[i][j]==1:
                    self.h1(i,j,visited)
                    c+=1
        return c




grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


grid2= [
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,1,0,0],
  [0,0,0,1,1]
]

grid1 = [
  [1,1,1,1,0],
  [1,1,0,1,0],
  [1,1,0,0,0],
  [0,0,0,0,0]
]

grid3 = [
  [1,1,0,1,0,0],
  [1,1,0,1,0,0],
  [1,1,0,0,0,0],
  [1,0,1,0,1,0],
  [1,0,0,0,1,0],
]


#assign grid1 or grid2 in grid 
grid=grid3

row=len(grid)
col=len(grid[0])

p= ShubhamGraph(row,col,grid)
print(p.countiland())
