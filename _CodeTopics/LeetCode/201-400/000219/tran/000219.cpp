class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {

        unordered_map<int, vector<int>> dic;
        for (int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            // C++ 判断map里是否有某个key是用map的count()方法。
            // 当然，也可以用 map 自己的 find 方法。
            if (dic.count(num)) {
                if (i - dic[num].back() <= k) {
                    return true;
                } else {
                    dic[num].push_back(i);
                }
            } else {
                dic[num] = vector<int>{i};
            }
        }
        return false;
    }
};

/*
https://leetcode-cn.com/submissions/detail/260013517/

执行用时：220 ms, 在所有 C++ 提交中击败了10.70%的用户
内存消耗：94.9 MB, 在所有 C++ 提交中击败了5.03%的用户
通过测试用例：
51 / 51
*/
