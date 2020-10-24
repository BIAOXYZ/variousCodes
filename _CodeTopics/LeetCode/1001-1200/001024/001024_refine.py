class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        
        # 其实flag这个标志不是必须的：只要经过内层while循环后还是无法更新一个更大的start，
        # 那就说明条件是无法满足的，比如：
        #     clips = [[0,1],[0,5],[1,2],[2,3],[3,5],[6,8],[7,10]], T = 10
        # 第一次内层while循环选中[0,5]，第二次不论从哪个出发，都最多只能到5，也就是无法更新
        # 一个更大的start，此时后面的[6,8]，[7,10]之类的是接不上去的，所以就不可能完成任务。

        newclips = sorted(clips)
        length = len(clips)
        res = 0
        start, clipIndex = 0, 0

        while start < T and clipIndex <= length - 1:
            nextStart = start
            while newclips[clipIndex][0] <= start:
                nextStart = max(nextStart, newclips[clipIndex][1])
                clipIndex += 1
                if clipIndex > length - 1:
                    break
            if nextStart == start:
                return -1
            start = nextStart
            res += 1
        
        if start < T:
            return -1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/118277826/

52 / 52 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.2 MB

执行用时：24 ms, 在所有 Python 提交中击败了43.37%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.26%的用户
"""
