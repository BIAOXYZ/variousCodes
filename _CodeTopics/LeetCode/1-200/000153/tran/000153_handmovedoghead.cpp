#include <algorithm>
class Solution {
public:
    int findMin(vector<int>& nums) {

        // C++ 手动狗头题。
        return *(std::min_element(nums.begin(), nums.end()));
    }
};

/*
https://leetcode-cn.com/submissions/detail/165079052/

150 / 150 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 10 MB

执行用时：8 ms, 在所有 C++ 提交中击败了29.71%的用户
内存消耗：10 MB, 在所有 C++ 提交中击败了22.62%的用户
*/
