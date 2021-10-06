class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 手动狗头题
        return len(s.split(' ')) if s.count(' ') != len(s) else 0
        
"""
https://leetcode-cn.com/submissions/detail/226337377/

19 / 27 个通过测试用例
状态：解答错误

输入：
"Of all the gin joints in all the towns in all the world,   "
输出：
16
预期结果：
13
"""
