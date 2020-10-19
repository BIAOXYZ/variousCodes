
`309. 最佳买卖股票时机含冷冻期` https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/zui-jia-mai-mai-gu-piao-shi-ji-han-leng-dong-qi-4/
- >
  ```
  对于力扣平台上的股票类型的题目：

  121. 买卖股票的最佳时机
  122. 买卖股票的最佳时机 II
  123. 买卖股票的最佳时机 III
  188. 买卖股票的最佳时机 IV
  （本题）309. 最佳买卖股票时机含冷冻期
  714. 买卖股票的最佳时机含手续费
  剑指 Offer 63. 股票的最大利润

  一种常用的方法是将「买入」和「卖出」分开进行考虑：「买入」为负收益，而「卖出」为正收益。在初入股市时，你只有「买入」的权利，
  只能获得负收益。而当你「买入」之后，你就有了「卖出」的权利，可以获得正收益。显然，我们需要尽可能地降低负收益而提高正收益，
  因此我们的目标总是将收益值最大化。因此，我们可以使用动态规划的方法，维护在股市中每一天结束后可以获得的「累计最大收益」，
  并以此进行状态转移，得到最终的答案。
  ```
- [x] 方法一：动态规划

『图解』DP 思路，学习了状态机的解法 https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/dp-zhuang-tai-de-ding-yi-you-liang-chong-fang-fa-b/
