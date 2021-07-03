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
    // 这个是从网上抄了一段模板实现的，比较通用，试试可以的话就留着自用了- -
    // https://stackoverflow.com/questions/8483985/obtaining-list-of-keys-and-values-from-unordered-map/33941694#33941694

    template<typename myMap>
    std::vector<typename myMap::key_type> Keys(const myMap& m)
    {
        std::vector<typename myMap::key_type> r;
        r.reserve(m.size());
        for (const auto&kvp : m)
        {
            r.push_back(kvp.first);
        }
        return r;
    }

    string frequencySort(string s) {
        unordered_map<char, int> dic = str_to_dic(s);
        vector<char> keys = Keys(dic);

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
https://leetcode-cn.com/submissions/detail/191876126/

32 / 32 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 8.5 MB

执行用时：16 ms, 在所有 C++ 提交中击败了49.32%的用户
内存消耗：8.5 MB, 在所有 C++ 提交中击败了49.14%的用户
*/
