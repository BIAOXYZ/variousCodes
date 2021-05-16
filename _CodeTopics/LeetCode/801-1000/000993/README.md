
`993. 二叉树的堂兄弟节点` https://leetcode-cn.com/problems/cousins-in-binary-tree/solution/er-cha-shu-de-tang-xiong-di-jie-dian-by-mfh2d/
- [ ] 方法一：深度优先搜索
- [x] 方法二：广度优先搜索

# 测试用例

```
[1,2,3,4]
4
3
[1,2,3,null,4,null,5]
5
4
[1,2,3,null,4]
2
3
```

# `000993.py`

虽然这个也是 BFS，但是和答案的 BFS 实现还是不一样的，我的实现要简单得多，因为既不需要维护深度，也不需要维护父节点——话说回来，这题一般的解法既要考虑深度，又要维护父节点信息，怎么看也不应该是easy吧。。。
