class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        length = len(numbers)
        dic = dict()
        for i in range(length):
            another = target - numbers[i]
            if dic.has_key(another):
                return [dic[another]+1, i+1]
            else:
                dic[numbers[i]] = i
        # 由于肯定有且只有一组结果，所以其实下面这个return就没用了
        return []
        
"""
https://leetcode-cn.com/submissions/detail/89729183/

17 / 17 个通过测试用例
状态：通过
执行用时：16 ms
内存消耗：13.6 MB
"""
"""
执行用时：16 ms, 在所有 Python 提交中击败了93.06%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了10.00%的用户
"""
