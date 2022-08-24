import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        n = len(arr)
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[n-k:]
        
        res = []
        ind = bisect.bisect_right(arr, x)
        left, right = ind - 1, ind
        while left >= 0 and right <= n-1 and len(res) < k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
        while len(res) < k:
            if left == -1:
                res.extend(arr[right:right+k-len(res)])
            elif right == n:
                res.extend(arr[left-k+len(res)+1:left+1])
        return sorted(res)
        
"""
https://leetcode.cn/submissions/detail/354561880/

执行用时：
56 ms
, 在所有 Python3 提交中击败了
61.67%
的用户
内存消耗：
16.4 MB
, 在所有 Python3 提交中击败了
16.10%
的用户
通过测试用例：
66 / 66
"""
