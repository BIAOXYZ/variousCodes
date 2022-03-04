class Solution {
public:
    long long subArrayRanges(vector<int>& nums) {

        // 第 271 场周赛第二题
        // https://leetcode-cn.com/submissions/detail/247648046/

        int n = nums.size();
        if (n == 1)
            return 0;
        
        vector<long long> dp(n, 0);
        dp[0] = 0;
        dp[1] = abs(nums[1] - nums[0]);
        for (int i = 2; i < n; ++i) {
            // 发现是这个 incr 也得用 long long 改一下。。。
            long long incr = 0;
            int currMax = nums[i], currMin = nums[i];
            for (int j = i-1; j > -1; --j) {
                currMax = max(currMax, nums[j]);
                currMin = min(currMin, nums[j]);
                incr += currMax - currMin;
            }
            dp[i] = dp[i-1] + incr;
        }
        return dp[n-1];
    }
};

/*
https://leetcode-cn.com/submissions/detail/277390874/

执行用时：88 ms, 在所有 C++ 提交中击败了48.15%的用户
内存消耗：10.6 MB, 在所有 C++ 提交中击败了24.43%的用户
通过测试用例：
71 / 71
*/
