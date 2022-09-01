class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {

        // 第 28 场双周赛第一题
        // https://leetcode-cn.com/submissions/detail/78709545/

        int n = prices.size();
        if (n == 1)
            return prices;

        vector<int> res(n, 0);
        for (int i = 0; i < n; ++i) {
            res[i] = prices[i];
            for (int j = i+1; j < n; ++j) {
                if (prices[j] <= prices[i]) {
                    res[i] = prices[i] - prices[j];
                    break;
                }
            }
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/357836686/

执行用时：
4 ms
, 在所有 C++ 提交中击败了
81.96%
的用户
内存消耗：
9.5 MB
, 在所有 C++ 提交中击败了
96.20%
的用户
通过测试用例：
103 / 103
*/
