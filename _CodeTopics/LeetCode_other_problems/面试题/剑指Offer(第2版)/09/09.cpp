class CQueue {
    vector<int> queue;
public:
    CQueue() {
        
    }
    
    void appendTail(int value) {
        queue.push_back(value);
    }
    
    int deleteHead() {
        if (queue.empty()) {
            return -1;
        }
        int rt = queue[0];
        queue.erase(queue.begin());
        return rt;
    }
};

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue* obj = new CQueue();
 * obj->appendTail(value);
 * int param_2 = obj->deleteHead();
 */
 
/*
https://leetcode-cn.com/submissions/detail/83397651/

55 / 55 个通过测试用例
状态：通过
执行用时：704 ms
内存消耗：103.3 MB
*/
/*
// C++果然是效率亲儿子。。。

执行用时：704 ms, 在所有 C++ 提交中击败了60.55%的用户
内存消耗：103.3 MB, 在所有 C++ 提交中击败了100.00%的用户
*/
