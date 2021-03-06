'''
数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。

示例 1：

输入：[1,2,5,9,5,9,5,5,5]
输出：5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-majority-element-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        for i in nums:
            dict[i]=dict.get(i,0)+1
        for key,value in dict.items():
            if value>len(nums)/2:
                return key
        return -1

nums =[8,8,7,7,7]
Solution().majorityElement(nums)