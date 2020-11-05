class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        def calculate_number_of_one(num):
            res = 0
            while num > 0:
                if num % 2 != 0:
                    res += 1
                # 这里也可以用移位操作符 >>
                num = num / 2
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
https://leetcode-cn.com/submissions/detail/121371335/

77 / 77 个通过测试用例
状态：通过
执行用时: 48 ms
内存消耗: 13.1 MB

执行用时：48 ms, 在所有 Python 提交中击败了26.88%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了24.45%的用户
"""
