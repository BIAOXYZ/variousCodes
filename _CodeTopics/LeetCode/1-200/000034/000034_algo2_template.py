class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 感觉自己发现的这个写法还是很清晰的，希望是无瑕疵的。

        def binary_search_leftmost_equal(arr, x):
            le, ri = 0, len(arr)-1
            res = -1
            while le <= ri:
                mid = le + (ri - le) / 2
                if arr[mid] > x:
                    ri = mid - 1
                elif arr[mid] < x:
                    le = mid + 1
                else:
                    # 如果是最plain的二分查找，这个else分支直接 return mid 就结束了。
                    ri = mid - 1
                    res = mid
            return res
            
        def binary_search_rightmost_equal(arr, x):
            le, ri = 0, len(arr)-1
            res = -1
            while le <= ri:
                mid = le + (ri - le) / 2
                if arr[mid] > x:
                    ri = mid - 1
                elif arr[mid] < x:
                    le = mid + 1
                else:
                    le = mid + 1
                    res = mid
            return res
        
        return [binary_search_leftmost_equal(nums, target), binary_search_rightmost_equal(nums, target)]
        
"""
https://leetcode-cn.com/submissions/detail/151737920/

88 / 88 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.3 MB

执行用时：20 ms, 在所有 Python 提交中击败了67.94%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了79.36%的用户
"""
"""
注：且不管效率如何（其实也不算差），这个算法的实现真的觉得写得还是很清晰易读易懂的，以后二分查找左边界/右边界就用这个模板。
"""
