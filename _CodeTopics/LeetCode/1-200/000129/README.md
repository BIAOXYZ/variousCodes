
`129. 求根到叶子节点数字之和` https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/solution/qiu-gen-dao-xie-zi-jie-dian-shu-zi-zhi-he-by-leetc/
- [x] 方法一：深度优先搜索 【其实我的实现`000129.py`更准确说是`回溯+DFS`，但是看了眼答案还是复杂了，纯DFS就能搞定】
- 方法二：广度优先搜索

# 测试用例

```
[1,2,3]
[4,9,0,5,1]
[]
[1]
[1,2]
```

# `000129.py`

如前所述，这种`回溯+DFS`的实现还是复杂了，纯DFS就可以。

另外回头对比下这个和`000113.py`，我感觉这两个的核心函数很相似，但是回溯完pop()元素的时候却不一样了。回头对比下为啥。
