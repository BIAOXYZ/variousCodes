class Solution {
public:
    int minPairSum(vector<int>& nums) {
        
        // 第 53 周双周赛第二题。这里直接翻译了当时的python实现：
        // https://leetcode-cn.com/submissions/detail/182013482/
        
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int res = 0;
        for (int i = 0; i < n/2; ++i) {
            res = max(res, nums[i] + nums[n-1-i]);
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/197613391/

37 / 37 个通过测试用例
状态：通过
执行用时: 220 ms
内存消耗: 94.1 MB

执行用时：220 ms, 在所有 C++ 提交中击败了97.90%的用户
内存消耗：94.1 MB, 在所有 C++ 提交中击败了24.65%的用户
*/
