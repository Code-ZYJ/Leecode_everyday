'''
给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。

注意：请不要在超过该数组长度的位置写入元素。

要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。

 

示例 1：

输入：[1,0,2,3,0,4,5,0]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/duplicate-zeros
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        j = len(arr)
        while i < j:
            if arr[i] == 0:
                arr.insert(i, 0)    #加了一个0，就删除一个末尾
                arr.pop()
                i += 2
            else:
                i += 1

arr=[1,0,2,3,0,4,5,0]
Solution().duplicateZeros(arr)
