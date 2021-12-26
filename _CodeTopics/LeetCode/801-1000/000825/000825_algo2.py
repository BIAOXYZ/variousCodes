class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """

        # 参考了官方答案的排序+双指针实现

        def satisfy_conditions_to_send_application(ageX, ageY):
            return 0.5 * ageX + 7 < ageY <= ageX
        
        length = len(ages)
        ages.sort()
        res = 0
        left = right = 0

        for i in range(length):
            if ages[i] < 15:
                continue
            while not satisfy_conditions_to_send_application(ages[left], ages[i]):
                left += 1
            if right < left:
                right = left
            while right < length and satisfy_conditions_to_send_application(ages[right], ages[i]):
                right += 1
            res += right - left - 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/252321905/

执行用时：208 ms, 在所有 Python 提交中击败了17.65%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了5.88%的用户
通过测试用例：
88 / 88
"""
