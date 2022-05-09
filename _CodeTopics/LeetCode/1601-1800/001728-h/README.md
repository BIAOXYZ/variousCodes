
`1728. 猫和老鼠 II` https://leetcode.cn/problems/cat-and-mouse-ii/solution/mao-he-lao-shu-ii-by-leetcode-solution-e5io/
- [ ] 方法一：拓扑排序

# 其他

https://leetcode.cn/problems/cat-and-mouse-ii/solution/mao-he-lao-shu-ii-by-leetcode-solution-e5io/1552794
- > 这道题的难度有多离谱呢？当时国服近3800人参赛，仅有22人AK，其中有1/3是比赛即将结束时极限AK。另外，虽然题目说的是1000步，但如果用动态规划思想，把步数上限设成1000是会TLE的，而“如果老鼠能获胜，必然会在X步内获胜”的X的具体取值无法证明（认为X不超过棋盘大小的2倍的做法只是因为题目数据范围太小无法构造反例，和1240题错误的DP可以通过是类似的），所以即使比赛期间AC的代码也不都是正确的，这道题的正解只能是官解的做法。建议没拿过guardian徽章的刷题者们收藏+CV吧。

https://leetcode.cn/problems/cat-and-mouse-ii/solution/mao-he-lao-shu-ii-by-leetcode-solution-e5io/1554511
- > 看到标题就想到了 [913. 猫和老鼠](https://leetcode.cn/problems/cat-and-mouse/) 当时也是CV的
- > 913第一次看到两个dfs互相嵌套，直接把我看傻眼了
- > 本题看到数据范围的第一反应是暴搜，但又看到条件4，老鼠1000次直接false就知道要跪了。
- > 之前打ACM的时候看到有大佬解题时用以一定时器放在while中，当快超时之前break掉，不知到能不能用于本题
