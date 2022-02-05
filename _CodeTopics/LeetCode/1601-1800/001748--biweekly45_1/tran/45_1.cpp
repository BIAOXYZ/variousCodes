class Solution {
public:
    int sumOfUnique(vector<int>& nums) {

        // 第 45 场双周赛第一题
        // https://leetcode-cn.com/submissions/detail/144244758/

        // 先来个匿名函数都不带引用的试试性能，等会都再加上引用试试。
        std::function<unordered_map<int, int>(vector<int>)> list_to_dic;
        list_to_dic = [](vector<int> lis) -> unordered_map<int, int> {
            unordered_map<int, int> dic{};
            for (auto elem : lis) {
                if (dic.find(elem) != dic.end()) {
                    ++dic[elem];
                } else {
                    dic[elem] = 1;
                }
            }
            return dic;
        };
        
        unordered_map<int, int> dic = list_to_dic(nums);
        int res = 0;
        for (auto [k, v] : dic) {
            if (v == 1) {
                res += k;
            }
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/265066804/

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：8 MB, 在所有 C++ 提交中击败了5.05%的用户
通过测试用例：
73 / 73
*/
