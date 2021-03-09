'''
统计所有小于非负整数 n 的质数的数量。
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 定义数组标记是否是质数
        is_prime = [1] * n

        count = 0
        for i in range(2, n):
            # 将质数的倍数标记为合数
            if is_prime[i]:
                count += 1
                # 从 i*i 开始标记
                for j in range(i * i, n, i):
                    is_prime[j] = 0

        return count

n = 10
Solution().countPrimes(499979)

