'''
给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。
'''
class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if (low%2==0 and high%2==1) or (low%2==1 and high%2==0):
            return int(high-low+1)/2
        if low%2==1 and high%2==1:
            return int(high-low-2)/2+2
        if low%2==0 and high%2==0:
            return int(high-low)/2

low = 3
high = 7
Solution().countOdds(low,high)