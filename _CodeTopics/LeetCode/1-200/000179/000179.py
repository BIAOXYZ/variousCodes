class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        # 这个题是真服了。。。上一个实现（`WA--000179`）辛辛苦苦写了一个比较函数 `relative_compare`，结果碰到
        #    极品测试用例 [34323,3432] 直接挂，而且看起来按照那个思路的话很不好修。
        # 这次的 `relative_compare2` 倒是简单粗暴，估计基本过也没问题，但是感觉太没技术含量了。

        def relative_compare2(str1, str2):
            if str1 + str2 > str2 + str1:
                return -1
            elif str1 + str2 < str2 + str1:
                return 1
            else:
                return 0

        strs = map(lambda x : str(x), nums)
        strs.sort(relative_compare2)
        # 服了，还有这么个用例[0,0]，太jian了。。。
        if strs[0] == "0":
            return "0"
        return "".join(strs)
        
"""
https://leetcode-cn.com/submissions/detail/166697992/

229 / 229 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.9 MB

执行用时：16 ms, 在所有 Python 提交中击败了98.85%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了71.06%的用户
"""
