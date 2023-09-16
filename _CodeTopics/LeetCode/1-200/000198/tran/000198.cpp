class Solution {
public:
    int rob(vector<int>& nums) {

        // https://leetcode-cn.com/submissions/detail/106465470/
        int length = nums.size();
        if (length == 0)
            return 0;
        else if (length == 1)
            return nums[0]; 
        
        vector<int> dp(length, 0);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        for (int i = 2; i < length; ++i)
            dp[i] = max(nums[i] + dp[i-2], dp[i-1]);
        return dp[length-1];
    }
};

/*
https://leetcode.cn/problems/house-robber/submissions/466818619/

时间
详情
0ms
击败 100.00%使用 C++ 的用户
内存
详情
7.86MB
击败 5.04%使用 C++ 的用户
*/
