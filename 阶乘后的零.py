'''给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 0
        while n >= 5:
            n = n // 5
            p += n
        return p

n = 3
Solution().trailingZeroes(n)