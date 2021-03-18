'''
给你一个偶数长度的字符串 s 。将其拆分成长度相同的两半，前一半为 a ，后一半为 b 。

两个字符串 相似 的前提是它们都含有相同数目的元音（'a'，'e'，'i'，'o'，'u'，'A'，'E'，'I'，'O'，'U'）。注意，s 可能同时含有大写和小写字母。

如果 a 和 b 相似，返回 true ；否则，返回 false 。

 

示例 1：

输入：s = "book"
输出：true
解释：a = "bo" 且 b = "ok" 。a 中有 1 个元音，b 也有 1 个元音。所以，a 和 b 相似。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/determine-if-string-halves-are-alike
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        voc=['a','e','i','o','u','A','E','I','O','U']
        a=s[:int(len(s)/2)]
        b=s[int((len(s)/2)):]
        sa=len([i for i in a if i in voc])
        sb=len([i for i in b if i in voc])
        if sa==sb:
            return True
        else:
            return False


s = "book"
Solution().halvesAreAlike(s)