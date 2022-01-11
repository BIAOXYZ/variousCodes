class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {

        int length = nums.size();
        vector dp(length, 1);

        for (int i = 1; i < length; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i])
                    dp[i] = max(dp[i], dp[j]+1);
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};

/*
https://leetcode-cn.com/submissions/detail/257495560/

执行用时：264 ms, 在所有 C++ 提交中击败了52.01%的用户
内存消耗：10.3 MB, 在所有 C++ 提交中击败了35.57%的用户
通过测试用例：
54 / 54
*/
