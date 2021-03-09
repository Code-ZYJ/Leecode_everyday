'''
给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。

请你统计并返回 grid 中 负数 的数目。


'''
class Solution(object):
    def countNegatives(self, grid):
        import numpy as np
        grid = np.array(grid)
        return int(grid.shape[0]*grid.shape[1]*(grid<0).mean())

grid = [[4,3,2,1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Solution().countNegatives(grid)