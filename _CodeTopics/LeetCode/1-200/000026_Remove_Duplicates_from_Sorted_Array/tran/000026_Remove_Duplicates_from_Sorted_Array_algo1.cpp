class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        if (nums.size() == 0) {
            return 0;
        }
        for (unsigned int i = nums.size() - 1; i > 0; --i) {
            if (nums[i] == nums[i-1]) {
                nums.erase(nums.begin() + i);
            }
        }
        return nums.size();
    }
};

/*
https://leetcode-cn.com/submissions/detail/169094137/

161 / 161 个通过测试用例
状态：通过
执行用时: 84 ms
内存消耗: 13.4 MB

执行用时：84 ms, 在所有 C++ 提交中击败了14.26%的用户
内存消耗：13.4 MB, 在所有 C++ 提交中击败了31.48%的用户
*/
