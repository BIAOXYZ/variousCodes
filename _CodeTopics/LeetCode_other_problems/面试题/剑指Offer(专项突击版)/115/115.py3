class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:

        n = len(nums)
        if n == 1:
            return True
        numberOfPrevElems = {i:0 for i in range(1, n+1)}
        ddic = defaultdict(list)
        for seq in sequences:
            if len(seq) == 1: continue
            for i in range(1, len(seq)):
                cur, pre = seq[i], seq[i-1]
                numberOfPrevElems[cur] += i
                # cur “依赖于” pre
                ddic[pre].append(cur)
                # 给 cur 也要做个假的key，下面 if 判断要用
                if cur not in ddic:
                    ddic[cur] = []
        
        # print(numberOfPrevElems)
        # print(ddic)
        if len(ddic.keys()) < n:
            return False
        q = [i for i in range(1, n+1) if numberOfPrevElems[i] == 0]
        while q:
            if len(q) != 1:
                return False
            currElem = q.pop()
            for elem in ddic[currElem]:
                numberOfPrevElems[elem] -= 1
                if numberOfPrevElems[elem] == 0:
                    q.append(elem)
        return True
        
"""
https://leetcode.cn/submissions/detail/340802211/

执行用时：
112 ms
, 在所有 Python3 提交中击败了
98.40%
的用户
内存消耗：
19.2 MB
, 在所有 Python3 提交中击败了
66.80%
的用户
通过测试用例：
83 / 83
"""
