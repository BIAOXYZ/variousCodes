
`1600. 皇位继承顺序` https://leetcode-cn.com/problems/throne-inheritance/solution/huang-wei-ji-cheng-shun-xu-by-leetcode-s-p6lk/
- [x] 方法一：多叉树的前序遍历

# 测试用例

```
["ThroneInheritance","birth","birth","birth","birth","birth","birth","getInheritanceOrder","death","getInheritanceOrder"]
[["king"],["king","andy"],["king","bob"],["king","catherine"],["andy","matthew"],["bob","alex"],["bob","asha"],[null],["bob"],[null]]
```

# `001600_ii.cpp`

通过使用C++的匿名函数来达到类似Python里“函数定义里套函数定义”的效果。
- 【[:star:][`*`]】 C++匿名函数的使用 https://www.cnblogs.com/yaya12138/p/11815475.html
- C++ 匿名函数 https://blog.csdn.net/zhang14916/article/details/101058089
- 深入浅出C++的function - 李超的文章 - 知乎 https://zhuanlan.zhihu.com/p/161356621
