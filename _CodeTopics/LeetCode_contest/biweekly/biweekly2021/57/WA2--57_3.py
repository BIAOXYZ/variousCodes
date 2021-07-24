class Solution(object):
    def splitPainting(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: List[List[int]]
        """

        n = 10**5
        diff = [0 for _ in range(n+1)]
        
        # 参照了这个人的思路：https://leetcode-cn.com/circle/discuss/pbqHVB/view/hHCNB9/
        # “第三题：类似差分数组。需要记录对应下标的累计值，同时用set记录所有的区间点。遍历求和，跳过非区间点，未求和前值非0时，把该区间加入res.”
        endpoints = set()
        for seg in segments:
            start, end, color = seg[0], seg[1], seg[2]
            diff[start] += color
            # 这里如果用 diff[end+1] -= color 很难处理，开始时就是用这个，各种问题
            diff[end] -= color
            endpoints.add(start)
            endpoints.add(end)
        
        prefixSum = [0]
        for i in range(1, n+1):
            prefixSum.append(prefixSum[-1] + diff[i])
        ##print prefixSum
        
        res = []
        left = 1
        for i in range(2, n+1):
            if prefixSum[i] == 0:
                res.append([left, i, prefixSum[left]])
                break
            if prefixSum[i] == prefixSum[left]:
                if i not in endpoints:
                    continue
                else:
                    res.append([left, i, prefixSum[left]])
                    left = i
            else:
                res.append([left, i, prefixSum[left]])
                left = i
        return res
        
```
https://leetcode-cn.com/submissions/detail/199462744/
  
11 / 66 个通过测试用例
状态：解答错误

输入：
[[4,5,9],[8,12,5],[4,7,19],[14,15,1],[3,10,8],[17,20,18],[7,19,14],[8,16,6],[14,17,7],[11,13,3]]
输出：
[[1,2,0]]
预期结果：
[[3,4,8],[4,5,36],[5,7,27],[7,8,22],[8,10,33],[10,11,25],[11,12,28],[12,13,23],[13,14,20],[14,15,28],[15,16,27],[16,17,21],[17,19,32],[19,20,18]]
```
