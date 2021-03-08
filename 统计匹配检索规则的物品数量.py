'''
给你一个数组 items ，其中 items[i] = [typei, colori, namei] ，描述第 i 件物品的类型、颜色以及名称。

另给你一条由两个字符串 ruleKey 和 ruleValue 表示的检索规则。

如果第 i 件物品能满足下述条件之一，则认为该物品与给定的检索规则 匹配 ：

ruleKey == "type" 且 ruleValue == typei 。
ruleKey == "color" 且 ruleValue == colori 。
ruleKey == "name" 且 ruleValue == namei 。
统计并返回 匹配检索规则的物品数量 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-items-matching-a-rule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        check = 0
        for i in range(len(items)):
            if ruleKey == 'type' and items[i][0] == ruleValue:
                check += 1
            if ruleKey == 'color' and items[i][1] == ruleValue:
                check += 1
            if ruleKey == 'name' and items[i][2] == ruleValue:
                check += 1
        return check

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
Solution().countMatches(items,ruleKey,ruleValue)