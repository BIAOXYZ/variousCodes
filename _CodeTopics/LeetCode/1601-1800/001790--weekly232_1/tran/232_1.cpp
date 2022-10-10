class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {

        // 第 232 场周赛第一题
        // https://leetcode.cn/submissions/detail/154892646/

        vector<int> ind = {};
        for (int i = 0; i < s1.size(); ++i) {
            if (s1[i] != s2[i]) {
                ind.push_back(i);
                if (ind.size() > 2) {
                    return false;
                }
            }
        }
        if (ind.empty() || (ind.size() == 2 && s1[ind[0]] == s2[ind[1]] && s1[ind[1]] == s2[ind[0]])) {
            return true;
        }
        return false;
    }
};

/*
https://leetcode.cn/submissions/detail/371773316/

执行用时：
4 ms
, 在所有 C++ 提交中击败了
17.66%
的用户
内存消耗：
6.1 MB
, 在所有 C++ 提交中击败了
24.69%
的用户
通过测试用例：
131 / 131
*/
