
`79. 单词搜索` https://leetcode-cn.com/problems/word-search/solution/dan-ci-sou-suo-by-leetcode-solution/
- [x] 方法一：深度优先搜索

在二维平面上使用回溯法（Python 代码、Java 代码） https://leetcode-cn.com/problems/word-search/solution/zai-er-wei-ping-mian-shang-shi-yong-hui-su-fa-pyth/

「手画图解」单词搜索 | DFS | 思路的产生和细节注意点 https://leetcode-cn.com/problems/word-search/solution/shou-hua-tu-jie-79-dan-ci-sou-suo-dfs-si-lu-de-cha/

# `WA--000079.py`

倒是记得在回溯算法里，当前状态返回后要做相应改变的。比如这里`currArr`最后一个元素在返回后应该再pop出去，但第一遍写的时候感觉这题应该比较特殊，推了一下好像不用再pop了。结果还是错了。

# `000079.py`

首先是改正了`WA--000079.py`里那个问题：函数调用返回后没有在上层函数里pop出去最后一个坐标。改完后程序就直接对了。

但是更值得一提的是这道题明显也用了DFS（同时加回溯算法），那么这道题和那些纯DFS的题（比如：`LC130`、`LC733`）有啥区别：
- [130. 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)
- [733. 图像渲染](https://leetcode-cn.com/problems/flood-fill/)

**根本区别就是**：
- 这道题你在每一个大步骤里，按照题目条件里给定的字符串中的下一个字符不断通过DFS往下试，一旦错了，必须要返回到上一个状态，并且把之前的选择取消掉（也就是修正这个状态，从而能正确进行下一次DFS）。
- 而纯DFS的题比如`LC130`和`LC733`都是你只管按DFS走，中间经过的符合条件的点都添加到一个全局的结果集里，所以**不涉及currArr这种当前的状态**（尽管这类算法里通常都会有一个visited数组来记录哪些点已经被访问过了，**但是这个也是全局状态，而不是每次函数一返回就要修正的那种当前状态**）。当走到某个走不下去的位置就直接开始一层层return即可。
