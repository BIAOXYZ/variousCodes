
`132. 分割回文串 II` https://leetcode-cn.com/problems/palindrome-partitioning-ii/solution/fen-ge-hui-wen-chuan-ii-by-leetcode-solu-norx/
- [x] 方法一：动态规划

# 测试用例

```
"aab"
"a"
"ab"
"x"
"xx"
"xxx"
"xxxx"
"aabc"
"cabababcbc"
```

# `WA--000132.py` and `000132.py`

这俩的差距就是第一次dp的时候第一个for循环，我的是正序，答案是倒序。但是我的有用例过不去，对错误用例 `"cabababcbc"` 来说，第一重dp完成后 `print dp` 的结果分别如下：
```console
我的：
[[True, False, False, False, False, False, False, True, False, True], 
 [True, True, False, True, False, True, False, False, False, False], 
 [True, True, True, False, True, False, True, False, True, False], 
 [True, True, True, True, False, True, False, False, False, False], 
 [True, True, True, True, True, False, True, False, True, False], 
 [True, True, True, True, True, True, False, False, False, False], 
 [True, True, True, True, True, True, True, False, True, False], 
 [True, True, True, True, True, True, True, True, False, True], 
 [True, True, True, True, True, True, True, True, True, False], 
 [True, True, True, True, True, True, True, True, True, True]
]

答案的：
[[True, False, False, False, False, False, False, False, False, False], 
 [True, True, False, True, False, True, False, False, False, False], 
 [True, True, True, False, True, False, True, False, False, False], 
 [True, True, True, True, False, True, False, False, False, False], 
 [True, True, True, True, True, False, True, False, False, False], 
 [True, True, True, True, True, True, False, False, False, False], 
 [True, True, True, True, True, True, True, False, True, False], 
 [True, True, True, True, True, True, True, True, False, True], 
 [True, True, True, True, True, True, True, True, True, False], 
 [True, True, True, True, True, True, True, True, True, True]
]
```
