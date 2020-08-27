class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []
        
        digit_letter_map = {
            2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'],
            6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']
        }

        def cartesian_of_string_list(l1,l2):
            if not l1 and l2:
                return l2
            elif not l2 and l1:
                return l1
            elif not l1 and not l2:
                return []
            tmp = []
            for s1 in l1:
                for s2 in l2:
                    tmp.append(s1 + s2)
            return tmp

        res = []
        for num in digits:
            l2 = digit_letter_map[int(num)]
            res = cartesian_of_string_list(res, l2)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/102195023/

25 / 25 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.7 MB
"""
"""
执行用时：16 ms, 在所有 Python 提交中击败了82.80%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了43.80%的用户
"""
