'''

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。



示例 1：

输入：[3,2,3]
输出：3
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
		dic = {}
		for i in nums:
			dic[i] = dic.get(i,0)+1
		for key,value in dic.items():
			if value > len(nums)/2:
				return key
nums = [2,2,1,1,1,2,2]
Solution().majorityElement(nums)