class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        
        sort(nums.begin(), nums.end());
        size_t length = nums.size();
        int res = INT_MAX;
        for (int i = 0; i < length - k + 1; ++i) {
            res = min(res, nums[i+k-1] - nums[i]);
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/266885610/

执行用时：12 ms, 在所有 C++ 提交中击败了88.69%的用户
内存消耗：13.3 MB, 在所有 C++ 提交中击败了56.56%的用户
通过测试用例：
118 / 118
*/
