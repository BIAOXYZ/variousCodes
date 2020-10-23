from collections import deque
class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """

        # 基本公式就是这个： [(a+1)+(a+k)]*k/2 = target。所以对于可能的连续序列 (a+1)...(a+k) 来说：
        # 如果序列长度 k 为奇数，那么 k 一定能够整除 target。
        # 如果序列长度 k 为偶数，那么 k 一定能够整除 target*2。

        num = target * 2
        res = []
        if target % 2 == 1:
            res.append([target/2, target/2+1])

        for sequenceLen in range(3, target):
            if sequenceLen % 2 == 1 and target % sequenceLen == 0:
                midnum = leftnum = rightnum = target / sequenceLen
                tmp = deque([midnum])
                appendflag = True
                for i in range(sequenceLen/2):
                    rightnum += 1; leftnum -= 1
                    if leftnum <= 0:
                        appendflag = False
                        break
                    tmp.append(rightnum); tmp.appendleft(leftnum)
                if appendflag:
                    res.append(list(tmp))
            elif sequenceLen % 2 == 0 and num % sequenceLen == 0:
                midsum = num / sequenceLen
                if midsum % 2 == 1:
                    leftnum, rightnum = midsum/2, midsum/2 + 1
                    tmp = deque([leftnum, rightnum])
                    appendflag = True
                    for i in range(sequenceLen/2-1):
                        rightnum += 1; leftnum -= 1
                        if leftnum <= 0:
                            appendflag = False
                            break
                        tmp.append(rightnum); tmp.appendleft(leftnum)
                    if appendflag:
                        res.append(list(tmp))
        res.sort()
        return res
        
"""
https://leetcode-cn.com/submissions/detail/118173777/

32 / 32 个通过测试用例
状态：通过
执行用时: 112 ms
内存消耗: 17.2 MB

执行用时：112 ms, 在所有 Python 提交中击败了43.35%的用户
内存消耗：17.2 MB, 在所有 Python 提交中击败了5.03%的用户
"""
