'''
给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。如果所有 1 都至少相隔 k 个元素，则返回 True ；否则，返回 False 。

 

示例 1：



输入：nums = [1,0,0,0,1,0,0,1], k = 2
输出：true
解释：每个 1 都至少相隔 2 个元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-all-1s-are-at-least-length-k-places-away
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
		n = len(nums)
		prev = -1
		for i in range(n):
			if nums[i] == 1:
				if prev != -1 and i - prev - 1 < k:
					return False
				prev = i
		return True

nums = [1,0,0,0,1,0,0,1]
k = 2
Solution().kLengthApart(nums,k)