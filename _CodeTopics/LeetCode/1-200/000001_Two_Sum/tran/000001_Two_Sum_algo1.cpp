class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++)
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target)
                    return vector<int> {i, j};
            }
        return vector<int> {};
    }
};

"""
https://leetcode-cn.com/submissions/detail/112953609/

29 / 29 个通过测试用例
状态：通过
执行用时: 612 ms
内存消耗: 8.8 MB

执行用时：612 ms, 在所有 C++ 提交中击败了34.97%的用户
内存消耗：8.8 MB, 在所有 C++ 提交中击败了49.32%的用户
"""
