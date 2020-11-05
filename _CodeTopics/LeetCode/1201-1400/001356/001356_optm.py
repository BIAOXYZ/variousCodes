class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        # 这个和之前的 001356.py 只有这个子函数实现上有差别。
        def calculate_number_of_one(num):
            res = 0
            while num > 0:
                res += num % 2
                num = num >> 1
            return res

        dic, res = {}, []
        for num in arr:
            numOfOne = calculate_number_of_one(num)
            if dic.has_key(numOfOne):
                dic[numOfOne].append(num)
            else:
                dic[numOfOne] = [num]
            
        for k in sorted(dic.keys()):
            res += sorted(dic[k])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/121371688/

77 / 77 个通过测试用例
状态：通过
执行用时: 44 ms
内存消耗: 13.2 MB

执行用时：44 ms, 在所有 Python 提交中击败了29.03%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了12.22%的用户
"""
