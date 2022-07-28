class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        if not arr:
            return []
        n = len(arr)
        arr2 = sorted(arr)
        
        ind = 1
        dic = {arr2[0]:1}
        for i in range(1, n):
            if arr2[i] > arr2[i-1]:
                ind += 1
                dic[arr2[i]] = ind
        arr = [dic[elem] for elem in arr]
        return arr
        
"""
https://leetcode.cn/submissions/detail/342771640/

执行用时：
104 ms
, 在所有 Python3 提交中击败了
29.70%
的用户
内存消耗：
31.6 MB
, 在所有 Python3 提交中击败了
96.37%
的用户
通过测试用例：
38 / 38
"""
