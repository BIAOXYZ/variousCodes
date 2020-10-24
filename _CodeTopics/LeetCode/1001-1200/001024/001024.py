class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        
        # 开始想用子函数的形式写，但是对于不能满足的情况怎么处理一直没写好，留着TODO吧。
        # 主要最近心情也不咋滴，垃圾资本家，呵呵。叶圣陶的《多收了三五斗》真是有先见之明。
        ##################################################
        # def video_stitch_from_to(currStart, clipIndex):
        #     if currStart >= T:
        #         return 0
        #     nextStart = start + 1
        #     isLegal = False
        #     while newclips[clipIndex][0] <= currStart:
        #         isLegal = True
        #         nextStart = max(nextStart, newclips[clipIndex][1])
        #         clipIndex += 1
        #     if not isLegal:
        #         return False
        #     else:
        #         return 1 + video_stitch_from_to(nextStart, clipIndex)
        #     return res

        newclips = sorted(clips)
        length = len(clips)
        res = 0
        start, clipIndex = 0, 0

        while start < T and clipIndex <= length - 1:
            flag = False
            nextStart = start
            while newclips[clipIndex][0] <= start:
                flag = True
                nextStart = max(nextStart, newclips[clipIndex][1])
                clipIndex += 1
                if clipIndex > length - 1:
                    break
            if nextStart == start:
                flag = False
            if not flag:
                return -1
            start = nextStart
            res += 1
        
        if start < T:
            return -1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/118274283/

52 / 52 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.8 MB

执行用时：16 ms, 在所有 Python 提交中击败了90.36%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了5.26%的用户
"""
