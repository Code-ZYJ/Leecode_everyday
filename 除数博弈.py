'''
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 False。假设两个玩家都以最佳状态参与游戏。

 

示例 1：

输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divisor-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        target = [0 for i in range(N + 1)]
        target[1] = 0  # 若爱丽丝抽到1，则爱丽丝输
        if N <= 1:
            return False
        else:

            target[2] = 1  # 若爱丽丝抽到2，则爱丽丝赢
            for i in range(3, N + 1):
                for j in range(1, i // 2):
                    # 若j是i的余数且target[i-j]为假（0）的话，则代表当前为真（1）
                    if i % j == 0 and target[i - j] == 0:
                        target[i] = 1
                        break
            return target[N] == 1

N=2
Solution().divisorGame(N)