'''

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。



示例 1：

输入：x = 121
输出：true
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
		return str(x) == str(x)[::-1]

x = 121
Solution().isPalindrome(x)