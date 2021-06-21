'''
给定两个数组，编写一个函数来计算它们的交集。



示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
'''


class Solution():
	def intersect(self, nums1, nums2):
		nums1.sort()
		nums2.sort()

		length1, length2 = len(nums1), len(nums2)
		intersection = list()
		index1 = index2 = 0
		while index1 < length1 and index2 < length2:
			if nums1[index1] < nums2[index2]:
				index1 += 1
			elif nums1[index1] > nums2[index2]:
				index2 += 1
			else:
				intersection.append(nums1[index1])
				index1 += 1
				index2 += 1

		return intersection

nums1 = [1,2,2,1]
nums2 = [2,2]
Solution().intersect(nums1,nums2)