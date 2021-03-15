'''
你有一个炸弹需要拆除，时间紧迫！你的情报员会给你一个长度为 n 的 循环 数组 code 以及一个密钥 k 。

为了获得正确的密码，你需要替换掉每一个数字。所有数字会 同时 被替换。

    如果 k > 0 ，将第 i 个数字用 接下来 k 个数字之和替换。
    如果 k < 0 ，将第 i 个数字用 之前 k 个数字之和替换。
    如果 k == 0 ，将第 i 个数字用 0 替换。

由于 code 是循环的， code[n-1] 下一个元素是 code[0] ，且 code[0] 前一个元素是 code[n-1] 。

给你 循环 数组 code 和整数密钥 k ，请你返回解密后的结果来拆除炸弹！



示例 1：

输入：code = [5,7,1,4], k = 3
输出：[12,10,16,13]
解释：每个数字都被接下来 3 个数字之和替换。解密后的密

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/defuse-the-bomb
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        ret = []
        extend_code = code + code
        n = len(code)
        for i in range(n):
            start = i + 1 if k >= 0 else n + k + i
            end = start + k if k >= 0 else n + i
            num = 0 if k == 0 else sum(extend_code[start:end])
            ret.append(num)
        return ret

code = [5,7,1,4]
k = 3
Solution().decrypt(code,k)