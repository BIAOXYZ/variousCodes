
`257. 二叉树的所有路径` https://leetcode-cn.com/problems/binary-tree-paths/solution/er-cha-shu-de-suo-you-lu-jing-by-leetcode-solution/
- [x] 方法一：深度优先搜索
- 方法二：广度优先搜索

赋值传值与引用传值 https://leetcode-cn.com/problems/binary-tree-paths/solution/fu-zhi-chuan-zhi-yu-yin-yong-chuan-zhi-by-vailing/

# 笔记

## `000257.py`

语法点：python字符串连接可以用加号，字符串截取似乎没有专门的办法，但是可以用下面这种：
```py
s1 = 'abcd'
s2 = 'xyz'

s1 = s1 + s2
print s1
s1 = s1[:-len(s2)]
print s2
--------------------------------------------------
abcdxyz
xyz
```

因为对于某个字符串`s`，`s[:-1]`其实就是“**右侧到倒数第一个字符，但是不包括这个字符**”，所以假设`s = 'abcdxyz'`，则`s[:-1] = 'abcdxy'`。因此，`s1[:-len(s2)]`就是右侧到倒数len(s2)，但是又不包括，相当于从`s1`中减掉`s2`。
