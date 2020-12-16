// https://troydhanson.github.io/uthash/
// leetcode的环境已经默认包含这个头文件了： #include "uthash.h"

struct htElement {
    int key;
    int val;
    UT_hash_handle hh;
};

void add_elem(struct htElement* dic, int k, int v) {
    struct htElement* kvPair;
    kvPair = malloc(sizeof(struct htElement));
    kvPair->key = k;
    kvPair->val = v;
    HASH_ADD_INT(dic, key, kvPair);
}
struct htElement *find_elem(struct htElement* dic, int k) {
    struct htElement *kvPair;
    HASH_FIND_INT(dic, &k, kvPair);
    return kvPair;
}

bool containsDuplicate(int* nums, int numsSize){
    struct htElement* dic = NULL;
    for (int i = 0; i < numsSize; i++) {
        struct htElement *kvPair;
        kvPair = find_elem(dic, nums + i);
        if (kvPair == NULL) {
            add_elem(dic, nums[i], i);
        }
        else {
            return true;
        }
    }
    return false;
}

/*
https://leetcode-cn.com/submissions/detail/131513279/

8 / 18 个通过测试用例
状态：解答错误

输入：
[1,2,3,1]
输出：
false
预期：
true
*/
/*
提交前已经知道肯定不对，但是一时没找到哪里不对（看起来是不会走进else分支，也就是往字典里添加元素没添加进去），打算先提交下做个标记。
真是服了，C的哈希表也太TM坑了。。。难用的一批。。。
*/
