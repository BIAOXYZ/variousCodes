class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 利用了桶排序的思想，但是其实还不如第一种实现（`000451.py`）方便。

        def str_to_dict_v2(s):
            res = {}
            for ch in s:
                res[ch] = res.setdefault(ch, 0) + 1
            return res
        dic = str_to_dict_v2(s)

        maxFreq = max(dic.values())
        buckets = [[] for _ in range(maxFreq + 1)]
        for k, v in dic.items():
            buckets[v].append(k)

        res = ''
        for i in range(maxFreq, 0, -1):
            bucket = buckets[i]
            for ch in bucket:
                res += ch * i
        return res
        
"""
https://leetcode-cn.com/submissions/detail/191888576/

32 / 32 个通过测试用例
状态：通过
执行用时: 44 ms
内存消耗: 21.4 MB

执行用时：44 ms, 在所有 Python 提交中击败了81.92%的用户
内存消耗：21.4 MB, 在所有 Python 提交中击败了11.86%的用户
"""
