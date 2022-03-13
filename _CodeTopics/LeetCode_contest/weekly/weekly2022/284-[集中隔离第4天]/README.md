
# 前言

`2022.03.07 周一`：下午正上着班呢，突然飞书上收到`字节应急`这个机器人的通知，让在中航广场高楼和矮楼办公的同学不要离开工区。后面的事情就不用再说了，高楼10层出了个阳性，然后全员被关在中航广场关了`两天一夜`或`三天两夜`，最晚的直到`3月9号`晚上才陆陆续续撤离完（这中间有差别：不在`505`个“被选出”的“密接”名单里的人3月8号晚“抽签”完就撤差不多了。我们这些在名单里的，最后一批离开的时间可能都到3月10号凌晨了——毕竟我是倒数第二批，我到隔离酒店的时候都`3月9号`23点多了）。

也因此，还是决定从`3月9号`算起，那么今天是集中隔离的`第4天`。

# 中国时间：2022-03-13 10:30

第 284 场周赛 https://leetcode-cn.com/contest/weekly-contest-284
- 6031. 找出数组中的所有 K 近邻下标 https://leetcode-cn.com/contest/weekly-contest-284/problems/find-all-k-distant-indices-in-an-array/
- 5203. 统计可以提取的工件 https://leetcode-cn.com/contest/weekly-contest-284/problems/count-artifacts-that-can-be-extracted/
- 5227. K 次操作后最大化顶端元素 https://leetcode-cn.com/contest/weekly-contest-284/problems/maximize-the-topmost-element-after-k-moves/
- 6032. 得到要求路径的最小带权子图 https://leetcode-cn.com/contest/weekly-contest-284/problems/minimum-weighted-subgraph-with-the-required-paths/

# (3)

这题被官方坑了，比赛中间改题目（改完后的版本更简单了，但是我一直是用改之前更难的版本啊- -）。。。详情见：

https://leetcode-cn.com/circle/discuss/3PMerp/view/y2ADKU/
- > 第三题题目改动过，原本的条件中要求重新放入栈中的元素不能出现在栈中，后来这个条件没了。因此 WA 了 6 发...
- > 强烈建议 Leetcode 有一个消息提醒机制，比赛中如果有题目变更，让选手收到一个弹窗。

```
[5,2,2,4,0,6]
4
[2]
1

[5,2,2,4,0,6]
6

[31,15,92,84,19,92,55]
4
```
