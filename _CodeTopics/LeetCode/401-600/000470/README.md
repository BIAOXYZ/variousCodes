
`470. 用 Rand7() 实现 Rand10()` https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/yong-rand7-shi-xian-rand10-by-leetcode-s-qbmd/
- [x] 方法一：拒绝采样

详细思路及优化思路分析，逐行解释 https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/xiang-xi-si-lu-ji-you-hua-si-lu-fen-xi-zhu-xing-ji/

从最基础的讲起如何做到均匀的生成随机数 https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/cong-zui-ji-chu-de-jiang-qi-ru-he-zuo-dao-jun-yun-/

【宫水三叶】k 进制诸位生成 + 拒绝采样 https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/gong-shui-san-xie-k-jin-zhi-zhu-wei-shen-zmd4/

【微扰理论】一个不均匀硬币如何抛能得到等概率事件🤔 https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/wei-rao-li-lun-yi-ge-bu-jun-yun-ying-bi-fo4ei/
- > 想到很久之前面试一家有趣的公司 老板（清华大佬）问过一个很简单的题目，大概意思是： 一个不均匀的硬币，怎么抛硬币可以让我们得到50% 50%的概率事件
- > 可能由于小时候做过类似的思考 几乎秒答：抛两次，先正后反记为1，先反后正记为2。 1和2就是等可能事件。 那么我们是如何避开硬币不均匀的事情的呢，本质就是我们拒绝了一部分事件，比如两次都是正面，或者都是反面。 如果碰到这样的情况，我们需要做的就是重新抛就行啦～

# 测试用例

```
1
2
3
10000
```
