class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """

        # 计数排序
        # 先统计待排序数组里的元素的频率，然后通过遍历“那个能确定先后顺序的数据结构”来不断往结果里贴。
        # 所以核心点是其实不涉及比较，因此不用遵守 O(NlogN) 的 bound。
        ctr = Counter(s)
        res = []
        for ch in order:
            if ch in ctr and ctr[ch] > 0:
                res.append(ch * ctr[ch])
                ctr[ch] = 0
        for ch, freq in ctr.items():
            if freq > 0:
                res.append(ch * freq)
        return ''.join(res)
        
"""
https://leetcode.cn/submissions/detail/381763681/

执行用时：
16 ms
, 在所有 Python 提交中击败了
82.35%
的用户
内存消耗：
13.1 MB
, 在所有 Python 提交中击败了
29.41%
的用户
通过测试用例：
39 / 39
"""
