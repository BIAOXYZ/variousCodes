class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        length = len(timePoints)
        if len(set(timePoints)) < length:
            return 0
        
        def calculate_diff(t1, t2):
            hours = int(t2[:2]) - int(t1[:2])
            minutes = int(t2[3:]) - int(t1[3:])
            minutes += hours * 60
            return min(minutes, 60*24 - minutes)
        
        timePoints.sort()
        # 这里按常理说应该是 mindiff = calculate_diff(timePoints[-1], timePoints[0]) 的，
        # 因为要第一个减去最后一个，但是 calculate_diff 假定了第二个入参更大。
        # 其实只要代入测试用例 ["23:59","00:00"] 就会得到 -1439，就知道为啥错了。
        mindiff = calculate_diff(timePoints[0], timePoints[-1])
        for i in range(1, length):
            mindiff = min(mindiff, calculate_diff(timePoints[i-1], timePoints[i]))
        return mindiff
        
"""
https://leetcode-cn.com/submissions/detail/259632531/

执行用时：32 ms, 在所有 Python3 提交中击败了93.10%的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了63.60%的用户
通过测试用例：
113 / 113
"""
