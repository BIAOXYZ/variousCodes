class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        people.sort(reverse=True)
        res = 0
        left, right = 0, len(people)-1
        while left < right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                left += 1
            res += 1
        
        if left == right:
            return res + 1
        elif left > right:
            return res
        
"""
https://leetcode-cn.com/submissions/detail/211724680/

78 / 78 个通过测试用例
状态：通过
执行用时: 92 ms
内存消耗: 17 MB

执行用时：92 ms, 在所有 Python 提交中击败了76.71%的用户
内存消耗：17 MB, 在所有 Python 提交中击败了45.20%的用户
"""
