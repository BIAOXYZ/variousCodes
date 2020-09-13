
`79. 单词搜索` https://leetcode-cn.com/problems/word-search/solution/dan-ci-sou-suo-by-leetcode-solution/
- [x] 方法一：深度优先搜索

在二维平面上使用回溯法（Python 代码、Java 代码） https://leetcode-cn.com/problems/word-search/solution/zai-er-wei-ping-mian-shang-shi-yong-hui-su-fa-pyth/

「手画图解」单词搜索 | DFS | 思路的产生和细节注意点 https://leetcode-cn.com/problems/word-search/solution/shou-hua-tu-jie-79-dan-ci-sou-suo-dfs-si-lu-de-cha/

# `WA--000079.py`

倒是记得在回溯算法里，当前状态返回后要做相应改变的。比如这里`currArr`最后一个元素在返回后应该再pop出去，但第一遍写的时候感觉这题应该比较特殊，推了一下好像不用再pop了。结果还是错了。
