class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {

        unordered_set<int> se;
        for (int i = 0; i < nums.size(); ++i) {
            if (i >= k+1) {
                se.erase(nums[i-k-1]);
            }
            if (se.count(nums[i])) {
                return true;
            }
            se.insert(nums[i]);
        }
        return false;
    }
};

/*
https://leetcode-cn.com/submissions/detail/260013841/

执行用时：124 ms, 在所有 C++ 提交中击败了96.63%的用户
内存消耗：70.5 MB, 在所有 C++ 提交中击败了86.91%的用户
通过测试用例：
51 / 51
*/
/*
mark！这道题确实是C++就是比Python慢，因为C++的 124ms 都超过 96.63% 了。
而前面两个Python版本的都是 88ms 却只能超过 51.37% 的用户。
*/
