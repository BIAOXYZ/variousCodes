class Solution {
public:
    unordered_map<char, int> str_to_dic(string s) {
        unordered_map<char, int> res;
        for (char ch : s) {
            if (res.find(ch) != res.end()) {
                res[ch] += 1;
            } else {
                res[ch] = 1;
            }
        }
        return res;
    }

    // C++ unordered_map 没有类似 Python 的 .keys(), .values() 接口。。。只能自己实现- -
    vector<char> get_list_of_keys(unordered_map<char, int> ump) {
        vector<char> res;
        for (auto kv : ump) {
            res.push_back(kv.first);
        }
        return res;
    }

    string frequencySort(string s) {
        unordered_map<char, int> dic = str_to_dic(s);
        vector<char> keys = get_list_of_keys(dic);

        // 匿名函数想要用外部变量dic，需要中括号里加 &。
        sort(keys.begin(), keys.end(), 
            [&](char x, char y) {
                return (dic[x] >= dic[y]);
            }
        );

        string res = (string)"";
        for (char key : keys) {
            for (int i = 0; i < dic[key]; ++i) {
                res += key;
            }
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/191873952/

32 / 32 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 8.6 MB

执行用时：20 ms, 在所有 C++ 提交中击败了24.46%的用户
内存消耗：8.6 MB, 在所有 C++ 提交中击败了46.96%的用户
*/
