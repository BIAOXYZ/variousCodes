class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def relative_compare(str1, str2):
            i, len1, len2 = 0, len(str1), len(str2)
            while i < len1 and i < len2:
                if str1[i] > str2[i]:
                    return -1
                elif str1[i] < str2[i]:
                    return 1
                i += 1
            if len1 < len2:
                for i in range(len1, len2):
                    if str1[-1] > str2[i]:
                        return -1
                    elif str1[-1] < str2[i]:
                        return 1
            elif len1 > len2:          
                for i in range(len2, len1):
                    if str1[i] > str2[-1]:
                        return -1
                    elif str1[i] < str2[-1]:
                        return 1
            return 0
        
        strs = map(lambda x : str(x), nums)
        strs.sort(relative_compare)
        return "".join(strs)
        
"""
https://leetcode-cn.com/submissions/detail/166696842/

221 / 229 个通过测试用例
状态：解答错误

输入：
[34323,3432]
输出：
"343233432"
预期：
"343234323"
"""
