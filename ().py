# 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：
#
# () 得 1 分。
# AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
# (A) 得 2 * A 分，其中 A 是平衡括号字符串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/score-of-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def scoreOfParentheses(self, S):
        return eval(S.replace(')(',')+(').replace('()','1').replace('(','2*('))
        """
        :type S: str
        :rtype: int
        """