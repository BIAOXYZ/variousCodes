class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {

        unordered_map<int, vector<int>> dic;
        for (int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            // C++ 判断map里是否有某个key是用map的count()方法。
            // 当然，也可以用 map 自己的 find 方法。 —— 这个就是了。。。
            //// if (dic.count(num)) {
            if (dic.find(num) != dic.end()) {
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
https://leetcode-cn.com/submissions/detail/260013656/

执行用时：200 ms, 在所有 C++ 提交中击败了18.99%的用户
内存消耗：95 MB, 在所有 C++ 提交中击败了5.03%的用户
通过测试用例：
51 / 51
*/
/*
这俩 C++ 的实现比同样的 Python 都慢啊。。。是因为直接传值没用引用的关系？
*/
