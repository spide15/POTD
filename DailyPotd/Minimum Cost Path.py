# Given a square grid of size N, each cell of which contains an integer cost that represents a cost to traverse through that cell, we need to find a path from the top left cell to the bottom right cell by which the total cost incurred is minimum.
# From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j). 
import heapq
class Solution:
    #Function to return the minimum cost to react at bottom
	#right cell from top left cell.
	def minimumCostPath(self, grid):
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pq = []
        heapq.heappush(pq, (grid[0][0], 0, 0))  # (cost, x, y)
        cost = [[float('inf')] * n for _ in range(n)]
        cost[0][0] = grid[0][0]
        while pq:
            current_cost, x, y = heapq.heappop(pq)
            if x == n-1 and y == n-1:
                return current_cost
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    new_cost = current_cost + grid[nx][ny]
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))
        return cost[n-1][n-1]
# 	def minimumCostPath(self, grid):
		#Code here


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.minimumCostPath(grid)
	print(ans)

# } Driver Code Ends