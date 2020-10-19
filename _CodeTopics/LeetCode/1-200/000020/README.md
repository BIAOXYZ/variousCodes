
`20. 有效的括号` https://leetcode-cn.com/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode-solution/
- [x] 方法一：栈

# 笔记

## `RE--000020.py`

这个之所以会RE主要是没有考虑到**当栈空了之后又来了右半边括号的情况：**比如`"]"`，`()]`等。

### 语法点：

python代码过长换行和shell脚本是类似的，都是末尾加`"\"`。但是过去一直以为回车后的新一行要空四格对齐，其实是不需要的。
