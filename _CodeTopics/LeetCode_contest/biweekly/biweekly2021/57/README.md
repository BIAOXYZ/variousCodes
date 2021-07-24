
# 中国时间：2021-07-24 22:30

第 57 场双周赛 https://leetcode-cn.com/contest/biweekly-contest-57
- 5804. 检查是否所有字符出现次数相同 https://leetcode-cn.com/contest/biweekly-contest-57/problems/check-if-all-characters-have-equal-number-of-occurrences/
- 5805. 最小未被占据椅子的编号 https://leetcode-cn.com/contest/biweekly-contest-57/problems/the-number-of-the-smallest-unoccupied-chair/
- 5806. 描述绘画结果 https://leetcode-cn.com/contest/biweekly-contest-57/problems/describe-the-painting/
- 5196. 队列中可以看到的人数 https://leetcode-cn.com/contest/biweekly-contest-57/problems/number-of-visible-people-in-a-queue/

# 其他

TNND，取消了大小周结果ld临时安排加班（之前已经明确说了不可能报的，连调休都不能）写文档，并且周六晚上开会对进展。。。结果我竟然忘了第一时间参加周赛，想起来时赶紧去报名参加，大概耽误了20分钟左右。

# (3)

```
[[1,4,5],[1,7,9]]
[[1,4,5],[2,3,9]]
[[1,4,5],[4,7,7]]
[[1,4,5],[4,7,7],[1,7,9]]
[[1,6,9],[6,7,24],[7,8,15],[8,10,7]]
[[1,4,5],[1,4,7],[4,7,1],[4,7,11]]
```

之前写的代码，diff数组那里如果要改变的是end+1，就很难处理，各种问题
```py
class Solution(object):
    def splitPainting(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # 看来前两天做的差分数组+前缀和用上了。。。
        
        n = 10**5
        diff = [0 for _ in range(n+1)]
        
        for seg in segments:
            start, end, color = seg[0], seg[1], seg[2]
            diff[start] += color
            diff[end+1] -= color
        
        prefixSum = [0]
        for i in range(1, n+1):
            prefixSum.append(prefixSum[-1] + diff[i])
        print prefixSum
        
        res = []
        left = 1
        leftVal = prefixSum[left]
        for i in range(2, n+1):
            if prefixSum[i] == 0:
                res.append([left, i-1, leftVal])
                break
            if prefixSum[i] == leftVal:
                continue
            else:
                res.append([left, i-1, leftVal])
                left = i - 1
                leftVal = prefixSum[left+1]
        return res
```
