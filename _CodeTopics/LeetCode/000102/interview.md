
# 1

`102. 二叉树的层序遍历` https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

# 2

C语言的整数溢出机制 - kong500的文章 - 知乎 https://zhuanlan.zhihu.com/p/28563004
```c
#include <stdio.h>
int main(int argc, const char* argv[])
{
    unsigned char x;
    x = 128 + 130;
    printf("%d\n", x);
}
--------------------------------------------------
main.c:13:9: warning: large integer implicitly truncated to unsigned type [-Woverflow]
2

...Program finished with exit code 0
Press ENTER to exit console.
```
