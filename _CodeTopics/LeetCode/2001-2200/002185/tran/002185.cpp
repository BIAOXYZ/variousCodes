class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {

        int res = 0;
        for (string& word : words) {
            if (word.compare(0, pref.size(), pref) == 0) {
                res++;
            }
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/393732047/

执行用时：
4 ms
, 在所有 C++ 提交中击败了
99.61%
的用户
内存消耗：
9.5 MB
, 在所有 C++ 提交中击败了
92.58%
的用户
通过测试用例：
95 / 95
*/
