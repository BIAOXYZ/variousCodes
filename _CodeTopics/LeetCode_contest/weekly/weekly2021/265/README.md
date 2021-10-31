
# 其他

这个 **`阿莫西林胶囊`** 真心牛！一盒四板其实吃到第二板感觉就不耳堵了，耳鸣也减轻了很多。但是还是决定把第三板也吃完。不过第四板就不吃了，感觉是药三分毒，能少吃还是少吃。但是耳鸣没有好kuoli，偶尔还是会有耳鸣的现象（其实之前偶尔也会耳鸣的，所以也不一定，也可能是已经完全好了，或者说已经完全消炎了），不过打算就这样了。主要是耳堵很烦人，这个解决了就好。

# 中国时间：2021-10-31 10:30

第 265 场周赛 https://leetcode-cn.com/contest/weekly-contest-265
- 5914. 值相等的最小索引 https://leetcode-cn.com/contest/weekly-contest-265/problems/smallest-index-with-equal-value/
- 5915. 找出临界点之间的最小和最大距离 https://leetcode-cn.com/contest/weekly-contest-265/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
- 5916. 转化数字的最小运算数 https://leetcode-cn.com/contest/weekly-contest-265/problems/minimum-operations-to-convert-number/
- 5917. 同源字符串检测 https://leetcode-cn.com/contest/weekly-contest-265/problems/check-if-an-original-string-exists-given-two-encoded-strings/

# (3)

前两题做完还有一个多小时，结果第三题改来改去，就是没改对，感觉就是记忆化搜索啊。。。这里贴下另外一部分代码，后面如果还复盘的话参考下吧：

```py
class Solution(object):
    def minimumOperations(self, nums, start, goal):
        """
        :type nums: List[int]
        :type start: int
        :type goal: int
        :rtype: int
        """
        
        dic = {}
        def memorize_search(currGoal, currNumOfTimes):
            if dic.has_key(currGoal):
                return dic[currGoal]
            if currGoal == start:
                dic[currGoal] = currNumOfTimes
                return dic[currGoal]
            if currGoal < 0 or currGoal > 1000:
                dic[currGoal] = float('inf')
                return dic[currGoal]
            tmpVal = float('inf')
            for num in nums:
                tmpVal = min(tmpVal, memorize_search(currGoal - num, currNumOfTimes + 1))
                tmpVal = min(tmpVal, memorize_search(currGoal + num, currNumOfTimes + 1))
                tmpVal = min(tmpVal, memorize_search(currGoal ^ num, currNumOfTimes + 1))
            dic[currGoal] = tmpVal
            return dic[currGoal]
        
        memorize_search(goal, 0)
        vals = dic.values()
        return -1 if min(vals) == float('inf') else min(vals)
```
