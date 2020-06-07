class Solution:
    def countSides(self, grid: List[List[int]], i: int, j: int) -> int:
        if grid[i][j] == 0: return 0
        result = 0
        if i == 0 or grid[i - 1][j] == 0: result += 1
        if i == len(grid) - 1 or grid[i + 1][j] == 0: result += 1
        if j == 0 or grid[i][j - 1] == 0: result += 1
        if j == len(grid[0]) - 1 or grid[i][j + 1] == 0: result += 1
        return result

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result += self.countSides(grid, i, j)
        return result
