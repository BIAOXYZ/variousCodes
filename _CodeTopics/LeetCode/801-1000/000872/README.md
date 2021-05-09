
`872. 叶子相似的树` https://leetcode-cn.com/problems/leaf-similar-trees/solution/xie-zi-xiang-si-de-shu-by-leetcode-solut-z0w6/
- [x] 方法一：深度优先搜索

# 测试用例

```
[3,5,1,6,2,9,8,null,null,7,4]
[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
[1]
[1]
[1]
[2]
[1,2]
[2,2]
[1,2,3]
[1,3,2]
```

# 其他

- 这题又照样了LeetCode官方的Bug：
  * 为什么某些测试用例下，执行代码返回结果正确，但提交解答却出错了 https://support.leetcode-cn.com/hc/kb/article/1194344/
- 这题还真就仅适合DFS——BFS肯定最终也是能做的，但是肯定要比常见的那些**同时适合DFS和BFS的题**里的常规BFS解法复杂的多。。。
