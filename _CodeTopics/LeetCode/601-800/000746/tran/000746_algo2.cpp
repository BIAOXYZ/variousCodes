class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {

        int length = cost.size();
        // C++ vector初始化一个长为length，值全为0的一维数组。 
        vector<int> dp(length, 0);
        dp[0] = cost[0];
        dp[1] = cost[1];

        for (int i = 2; i < length; i++) {
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i];
        }
        return min(dp[length-1], dp[length-2]);
    }
};

/*
https://leetcode-cn.com/submissions/detail/132683454/

276 / 276 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 13.6 MB

执行用时：8 ms, 在所有 C++ 提交中击败了92.51%的用户
内存消耗：13.6 MB, 在所有 C++ 提交中击败了19.32%的用户
*/
