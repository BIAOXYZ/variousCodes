#include <unordered_map>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        unordered_map<int, int> dic;
        for (int i = 0; i < nums.size(); i++) {
            if (dic.find(nums[i]) != dic.end()) {
                return true;
            }
            else {
                dic[nums[i]] = i;
            }
        }
        return false;
    }
};

/*
https://leetcode-cn.com/submissions/detail/130737830/

18 / 18 个通过测试用例
状态：通过
执行用时: 76 ms
内存消耗: 19.5 MB

执行用时：76 ms, 在所有 C++ 提交中击败了59.11%的用户
内存消耗：19.5 MB, 在所有 C++ 提交中击败了43.49%的用户
*/
