class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """

        # 曾经的第 222 周周赛第二题。
        # 这个提交基本复制了比赛里的提交（ https://leetcode-cn.com/submissions/detail/135559985/ ）。

        def list_to_dict(lis):
            dic = {}
            for num in lis:
                if dic.has_key(num):
                    dic[num] += 1
                else:
                    dic[num] = 1
            return dic
        dic = list_to_dict(deliciousness)

        res = 0
        res2 = 0
        keys = dic.keys()
        
        for num in keys:
            for i in range(22):
                if dic.has_key(2**i - num) and 2**i - num == num:
                    res2 += dic[num] * (dic[num] - 1) / 2
                    break
            for i in range(22):
                if dic.has_key(2**i - num) and 2**i - num != num:
                    res += dic[num] * dic[2**i - num]
        res /= 2
        res += res2
        return res % (10**9 + 7)
        
"""
https://leetcode-cn.com/submissions/detail/193049723/

70 / 70 个通过测试用例
状态：通过
执行用时: 672 ms
内存消耗: 20.5 MB

执行用时：672 ms, 在所有 Python 提交中击败了52.63%的用户
内存消耗：20.5 MB, 在所有 Python 提交中击败了63.16%的用户
"""
