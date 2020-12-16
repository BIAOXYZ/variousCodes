
`290. 单词规律` https://leetcode-cn.com/problems/word-pattern/solution/dan-ci-gui-lu-by-leetcode-solution-6vqv/
- [x] 方法一：哈希表

# 测试用例

```
"abba"
"dog cat cat dog"
"abba"
"dog cat cat fish"
"aaaa"
"dog cat cat dog"
"abba"
"dog dog dog dog"
"aaaa"
"dog dog dog dog"
```

# `000290.py`

只有一个要注意的点，对于如下输入：
```
"abba"
"dog dog dog dog"
```
之所以答案是False，是因为字母a已经和单词dog对应了，字母b就不能再和dog对应了。所以除了有个字典外，还得有个集合来进行这个条件的过滤。
