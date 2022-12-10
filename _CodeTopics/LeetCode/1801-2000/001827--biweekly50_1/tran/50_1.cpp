class Solution {
public:
    int minOperations(vector<int>& nums) {

        // 第 50 场双周赛第一题
        // https://leetcode.cn/submissions/detail/169039629/

        int length = nums.size();
        if (length == 1) {
            return 0;
        }

        int res = 0;
        for (int i = 1; i < length; ++i) {
            if (nums[i] > nums[i-1]) {
                continue;
            }
            int delta = abs(nums[i] - nums[i-1]) + 1;
            nums[i] += delta;
            res += delta;
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/388363440/

执行用时：
16 ms
, 在所有 C++ 提交中击败了
37.09%
的用户
内存消耗：
15.3 MB
, 在所有 C++ 提交中击败了
89.20%
的用户
通过测试用例：
94 / 94
*/
