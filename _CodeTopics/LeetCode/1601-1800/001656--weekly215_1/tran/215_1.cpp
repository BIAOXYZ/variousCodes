// 第 215 场周赛第一题
class OrderedStream {
public:
    int ptr;
    vector<string> arr;
public:
    OrderedStream(int n) {
        ptr = 1;
        arr.assign(n+1, "");
    }
    
    vector<string> insert(int idKey, string value) {
        arr[idKey] = value;
        if (arr[ptr] == "") {
            return vector<string>{};
        }
        int start = ptr;
        while (ptr <= arr.size()-1 && arr[ptr] != "") {
            ++ptr;
        }
        return vector<string>(arr.begin()+start, arr.begin()+ptr);
    }
};


/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream* obj = new OrderedStream(n);
 * vector<string> param_1 = obj->insert(idKey,value);
 */

/*
https://leetcode.cn/submissions/detail/350886066/

执行用时：
112 ms
, 在所有 C++ 提交中击败了
42.63%
的用户
内存消耗：
79 MB
, 在所有 C++ 提交中击败了
100.00%
的用户
通过测试用例：
101 / 101
*/
