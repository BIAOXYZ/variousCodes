class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:

        n = len(nums)
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
https://leetcode.cn/submissions/detail/340801471/

81 / 83 个通过测试用例
状态：解答错误

输入：
[1]
[[1]]
输出：
false
预期结果：
true
"""
