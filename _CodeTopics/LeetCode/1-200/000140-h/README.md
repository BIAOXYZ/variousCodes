
`140. 单词拆分 II` https://leetcode-cn.com/problems/word-break-ii/solution/dan-ci-chai-fen-ii-by-leetcode-solution/
- > 这道题是「139. 单词拆分」的进阶，第 139 题要求判断是否可以拆分，这道题要求返回所有可能的拆分结果。
- > 第 139 题可以使用动态规划的方法判断是否可以拆分，因此这道题也可以使用动态规划的思想。但是这道题如果使用***自底向上的动态规划的方法***进行拆分，则无法事先判断拆分的可行性，在不能拆分的情况下会超时。
- > 例如以下例子，由于字符串 s 中包含字母 b，而单词列表 wordDict 中的所有单词都由字母 a 组成，不包含字母 b，因此不能拆分，但是自底向上的动态规划仍然会在每个下标都进行大量的匹配，导致超时。
  ```console
  s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
  ```
- > 为了避免动态规划的方法超时，需要首先使用第 139 题的代码进行判断，在可以拆分的情况下再使用动态规划的方法进行拆分。相比之下，***自顶向下的记忆化搜索***可以在搜索过程中将不可以拆分的情况进行剪枝，因此记忆化搜索是更优的做法。
- [ ] 方法一：记忆化搜索

# 测试用例

```
"catsanddog"
["cat","cats","and","sand","dog"]
"pineapplepenapple"
["apple", "pen", "applepen", "pine", "pineapple"]
"catsandog"
["cats", "dog", "sand", "and", "cat"]
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
```

# 语法点

【[:star:][`*`]】 这个题官方答案里说明了`动态规划`和`记忆化搜索`的一个显著区别：dp是自底向上的，记忆化搜索是自顶向下的。

# `000140_algo2.py` = `000139_algo2.py` + `deliberate-TLE--000140.py` + 一个if判断

这个实现其实就是`LC139`的原版动态规划代码来判断是否能拆分，如果能，再加上之前纯回溯算法超时的原版代码。不过这个题的正解应该还是`记忆化搜索`，但是我实在太忙了，今天一天基本都在搞PBC库，没时间写了。留着TODO吧。
