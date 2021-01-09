
# 2021-01-09 22:30

第 43 场双周赛 https://leetcode-cn.com/contest/biweekly-contest-43
- 5633. 计算力扣银行的钱 https://leetcode-cn.com/contest/biweekly-contest-43/problems/calculate-money-in-leetcode-bank/
- 5634. 删除子字符串的最大得分 https://leetcode-cn.com/contest/biweekly-contest-43/problems/maximum-score-from-removing-substrings/
- 5635. 构建字典序最大的可行序列 https://leetcode-cn.com/contest/biweekly-contest-43/problems/construct-the-lexicographically-largest-valid-sequence/
- 5636. 重构一棵树的方案数 https://leetcode-cn.com/contest/biweekly-contest-43/problems/number-of-ways-to-reconstruct-a-tree/

# (3)

回溯的题没法单步调试实在太痛苦了。。。明天（记笔记时已经是“今天”了：`2021.01.10`）又是给资本家卖命的一天——到字节后第一个小周周日！没办法，拿命换钱。此外，以后周日的周赛应该改为一周参加，一周不参加了（比如明天——其实已经是“今天”了——的`第223场周赛`就不参加了），原因很简单，就是这个大小周。。。

## 技巧

言归正传，这道回溯算法题还是挺有代表性的：
1. 回溯 + 贪心。且贪心的对象要搞对：应该是结果列表的位置从低位到高位，而不是数字从大到小——当然，在某个确定的可用位置pos，数字num还是要按从大到小的顺序试的。
2. 只要贪心对象对了，找到的第一个结果肯定就是答案，此时就应该直接一层层结束，即使还有别的合法的序列，算法也不再执行下去了。以前还真没写过怎么提前结束回溯的，这次临时想到用了一个全局的flag，不过是比较cuo的flag。。。
3. 最终正确答案的终止条件是嵌在回溯的for循环里的，以前是单独的。不过这个应该也能改成单独的。
