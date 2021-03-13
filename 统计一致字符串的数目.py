'''
给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字符串 。
请你返回 words 数组中 一致字符串 的数目。

示例 1：

输入：allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
输出：2
解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-the-number-of-consistent-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        num=0
        for word in words:
            liset = list(set(word))
            for s in liset:
                flag=False
                if s not in allowed:
                    break
                flag=True
            if flag:
                num+=1
        return num

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

Solution().countConsistentStrings(allowed,words)