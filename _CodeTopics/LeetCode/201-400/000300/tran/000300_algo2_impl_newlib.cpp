class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {

        int length = nums.size();
        vector<int> d = {nums[0]};

        for (int i = 1; i < length; ++i) {
            if (nums[i] > d.back()) {
                d.push_back(nums[i]);
            } else {
                std::vector<int>::iterator loc = lower_bound(d.begin(), d.end(), nums[i]);
                // 也可以用 *loc = nums[i];
                d[loc - d.begin()] = nums[i];
            }
        }
        return d.size();
    }
};

/*
https://leetcode-cn.com/submissions/detail/257496079/

执行用时：8 ms, 在所有 C++ 提交中击败了90.55%的用户
内存消耗：10.2 MB, 在所有 C++ 提交中击败了66.86%的用户
通过测试用例：
54 / 54
*/
