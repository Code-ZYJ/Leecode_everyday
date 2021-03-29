'''给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。

 

示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-common-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = []
        min_length_char = min(A, key=len)
        for char in min_length_char:
            if all(char in item for item in A):
                res.append(char)
                A = [i.replace(char, '', 1) for i in A]

        return res

A=["bella","label","roller"]
Solution().commonChars(A)