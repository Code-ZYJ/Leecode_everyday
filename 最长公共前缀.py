'''编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
		pre = ''
		min_len = min([len(i) for i in strs])
		for i in range(min_len):
			for words in strs:
				if words[i] == strs[0][i]:
					flag = True
				else:
					flag = False
					break
			if flag:
				pre += strs[0][i]
			else:
				break
		return pre

strs = ["cir","car"]
Solution().longestCommonPrefix(strs)