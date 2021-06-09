'''
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
 

示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
		num = []
		X = x
		x = abs(x)
		out = 0
		while x != 0:
				num.append(x%10)
				#print(x%10)
				x = x//10
		for i in num:
				out = 10 * out + i
		if out>2**31:
				return 0

		elif X>=0:
				return out
		else:
				return -1*out

x = 1534236469
Solution().reverse(x)