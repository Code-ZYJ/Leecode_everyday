'''
给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。

输入为三个整数：day、month 和 year，分别表示日、月、年。

您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。

 

示例 1：

输入：day = 31, month = 8, year = 2019
输出："Saturday"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/day-of-the-week
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        days=-1    #因为后续算时间要减去一天，所以设置为-1
        #1971.1.1是周五
        res=['Friday','Saturday','Sunday','Monday','Tuesday','Wendnesday','Thrusday']
        for y in range(1971, year):
            if self.is_RUNyear(y):
                days += 366
            else:
                days += 365
        for m in range(1,month):
            if m==2:
                if self.is_RUNyear(year):
                    days+=29
                else:
                    days+=28
            elif m in [1,3,5,7,8,10,12]:
                days+=31
            else:
                days+=30
        days+=day
        return res[days%7]

    def is_RUNyear(self,year):
        if year % 400 == 0:
            return True
        if year % 4 == 0 and year % 100 != 0:
            return True
        return False

day,month,year=31,8,2019
Solution().dayOfTheWeek(day,month,year)