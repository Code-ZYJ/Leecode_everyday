'''
给你一个整数 n 。请你先求出从 1 到 n 的每个整数 10 进制表示下的数位和（每一位上的数字相加），然后把数位和相等的数字放到同一个组中。

请你统计每个组中的数字数目，并返回数字数目并列最多的组有多少个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-largest-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        S = [0 for _ in range(n + 1)]
        C = [0 for _ in range(37)]

        for i in range(1, n + 1):
            S[i] = S[i // 10] + i % 10
            C[S[i]] += 1

        x = max(C)
        return sum(i == x for i in C)

n=13
Solution().countLargestGroup(n)