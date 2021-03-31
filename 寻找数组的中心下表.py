'''
给你一个整数数组 nums，请编写一个能够返回数组 “中心下标” 的方法。

数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心下标，返回 -1 。如果数组有多个中心下标，应该返回最靠近左边的那一个。

注意：中心下标可能出现在数组的两端。

 

示例 1：

输入：nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
中心下标是 3 。
左侧数之和 (1 + 7 + 3 = 11)，
右侧数之和 (5 + 6 = 11) ，二者相等。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-pivot-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums[1:])==0:
            return 0
        for i in range(1,len(nums)):
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
        if sum(nums[:-1])==0:
            return len(nums)-1
        return -1

nums = [-1,-1,1,1,0,0]
Solution().pivotIndex(nums)
