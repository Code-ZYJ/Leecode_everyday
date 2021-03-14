'''给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。

通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。

 

示例 1：

输入：date = "2019-01-09"
输出：9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/day-of-the-year
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[-2:])
        total=0
        RUN_day = [31,29,31,30,31,30,31,31,30,31,30]    #第十二月不用算
        PIN_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        if self.is_RUNyear(year):
            for i in range(month-1):
                total += RUN_day[i]
        else:
            for i in range(month-1):
                total += PIN_day[i]
        total+=day
        return total


    def is_RUNyear(self,year):
        if year % 400 == 0:
            return True
        if year % 4 == 0 and year % 100 != 0:
            return True
        return False

date = "2019-01-09"
Solution().dayOfYear(date)