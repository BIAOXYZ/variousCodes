class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def merge_sort(nums):
            length = len(nums)
            if length < 2:
                return nums
            
            mid = length / 2
            leftArr = merge_sort(nums[:mid])
            rightArr = merge_sort(nums[mid:])
            res = []
            while leftArr and rightArr:
                if leftArr[0] < rightArr[0]:
                    res.append(leftArr.pop(0))
                else:
                    res.append(rightArr.pop(0))
            if leftArr:
                res.extend(leftArr)
            if rightArr:
                res.extend(rightArr)
            return res
        
        return merge_sort(nums)
        
"""
https://leetcode-cn.com/submissions/detail/125042896/

11 / 11 个通过测试用例
状态：通过
执行用时: 396 ms
内存消耗: 19.3 MB

执行用时：396 ms, 在所有 Python 提交中击败了5.12%的用户
内存消耗：19.3 MB, 在所有 Python 提交中击败了15.40%的用户
"""
"""
注：这个是参照wikipedia的python3实现些的。在写的时候就注意到了，在merge的时候会不断的pop(0)，效率肯定不行。。。
    应该是用两个index，每次index加一就好（或者至少要pop(0)的话别用list用deque啊）。
"""
