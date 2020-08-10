class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)
        res = 0
        zero_one_distribute_list = []

        i = 0
        while i < length:
            if i == length - 1:
                zero_one_distribute_list.append(1)
                break
            num_of_elem = 1
            j = i + 1
            while j < length:
                if s[j] == s[i]:
                    num_of_elem += 1
                    j += 1
                else:
                    zero_one_distribute_list.append(num_of_elem)
                    break
            if j == length:
                zero_one_distribute_list.append(num_of_elem)
                break
            else:
                i = j
        
        for i in range(len(zero_one_distribute_list) - 1):
            res += min(zero_one_distribute_list[i], zero_one_distribute_list[i+1])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/96505243/

90 / 90 个通过测试用例
状态：通过
执行用时：164 ms
内存消耗：14.1 MB
"""
"""
执行用时：164 ms, 在所有 Python 提交中击败了35.64%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了37.50%的用户
"""
