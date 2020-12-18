class Solution {
public:
    unordered_map<char, int> str_to_dic(string s) {
        unordered_map<char, int> dic;
        for (auto ch : s) {
            if (dic.find(ch) != dic.end()) {
                dic[ch]++;
            }
            else {
                dic[ch] = 1;
            }
        }
        return dic;
    }

    char findTheDifference(string s, string t) {
        unordered_map<char, int> dicS, dicT;
        dicS = str_to_dic(s);
        dicT = str_to_dic(t);
        for (auto kv = dicT.begin(); kv != dicT.end(); kv++) {
            if (dicS.find(kv->first) == dicS.end()) {
                return kv->first;
            }
            else if (kv->second > dicS[kv->first]) {
                return kv->first;
            }
        }
        return -1;
    }
};

/*
https://leetcode-cn.com/submissions/detail/131964426/

54 / 54 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 7.4 MB

执行用时：16 ms, 在所有 C++ 提交中击败了12.97%的用户
内存消耗：7.4 MB, 在所有 C++ 提交中击败了5.03%的用户
*/
