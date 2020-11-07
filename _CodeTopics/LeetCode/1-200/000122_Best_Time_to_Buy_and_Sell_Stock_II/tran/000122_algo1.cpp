class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int total = 0;
        for (int i = 0; i < prices.size() - 1; ++i) {
            if (prices[i+1] > prices[i])
                total += prices[i+1] - prices[i];
            else
                continue;
        }
        return total;
    }
};

/*
https://leetcode-cn.com/submissions/detail/121784155/

200 / 200 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 7.6 MB

执行用时：8 ms, 在所有 C++ 提交中击败了49.15%的用户
内存消耗：7.6 MB, 在所有 C++ 提交中击败了11.22%的用户
*/
