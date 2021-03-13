
`131. 分割回文串` https://leetcode-cn.com/problems/palindrome-partitioning/solution/fen-ge-hui-wen-chuan-by-leetcode-solutio-6jkv/
- [x] 方法一：回溯 + 动态规划预处理
- [x] 方法二：回溯 + 记忆化搜索

# 测试用例

```
"aab"
"x"
"xx"
"xxx"
"xxxx"
"aabc"
```

# 语法点

## `functools` 里的 `cache`

正如`000131_algo3_impl_newlib.py3`里说的那样：之前见到的都是 `@lru_cache(None)` 和 `@lru_cache()`，但这次官方答案里是用 `@cache`——目前还不知道有啥区别。。。不过似乎Python官方文档里有说。但是不准备往这里贴了，贴到另外一个仓库 `functools` 那里。
