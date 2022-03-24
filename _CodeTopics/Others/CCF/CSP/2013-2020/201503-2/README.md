
201503-2 http://118.190.20.162/view.page?gpid=T26
```
问题描述
　　给定n个整数，请统计出每个整数出现的次数，按出现次数从多到少的顺序输出。
输入格式
　　输入的第一行包含一个整数n，表示给定数字的个数。
　　第二行包含n个整数，相邻的整数之间用一个空格分隔，表示所给定的整数。
输出格式
　　输出多行，每行包含两个整数，分别表示一个给定的整数和它出现的次数。按出现次数递减的顺序输出。如果两个整数出现的次数一样多，则先输出值较小的，然后输出值较大的。
样例输入
12
5 2 3 3 1 3 4 2 5 2 3 5
样例输出
3 4
2 3
5 3
1 1
4 1
评测用例规模与约定
　　1 ≤ n ≤ 1000，给出的数都是不超过1000的非负整数。
```

# 原版
>> 有编译错误

```cpp
#include<bits/stdc++.h>

using namespace std;
typedef pair<int, int> PAIR;

bool com(const PAIR &a, const PAIR &b){
    if(a.second > b.second){
        return a.second > b.second;
    }
    else if(a.second == b.second){
        return a.first < b.first;
    }
}

void outint(int n){
    cout << n << ' ';
}

int main(){
    int n;
    cin >> n;

    vector<int> z;
    for(int i=0; i<n; i++){
        int z_i;
        cin >> z_i;
        z.emplace_back(z_i);
    }

    map<int,int> m;

    for(int i=0; i<n; i++){
        int key = z[i];
        if(m[key]){
            m[key]++;
        }
        else{
            m[key] = 1;
        }
    }
    vector<PAIR> vpair;

    //把map的值赋给向量
    for(map<int, int>::iterator it=m.begin();it!=m.end();it++)
    {
        vpair.push_back(make_pair(it->first, it->second));
    }

    //给向量排序
    sort(vpair.begin(), vpair.end(), com);
    //输出排好序的向量
    for_each(vpair.begin(), vpair.end(), outint);
    cout << endl;
    return 0;
}
```

# 修改后的版本

```cpp
#include<bits/stdc++.h>

using namespace std;
typedef pair<int, int> PAIR;

// bool com(const PAIR &a, const PAIR &b){
//     if(a.second > b.second){
//         return a.second > b.second;
//     }
//     else if(a.second == b.second){
//         return a.first < b.first;
//     }
// }

bool com(const PAIR &a, const PAIR &b){
    if(a.second != b.second){
        return a.second > b.second;
    }
    else if(a.second == b.second){
        return a.first < b.first;
    }
}

void outint(int n){
    cout << n << ' ';
}

int main(){
    int n;
    // cin >> n;

    // vector<int> z;
    // for(int i=0; i<n; i++){
    //     int z_i;
    //     cin >> z_i;
    //     z.emplace_back(z_i);
    // }

    n = 12;
    vector<int> z{5,2,3,3,1,3,4,2,5,2,3,5};

    map<int,int> m;

    for(int i=0; i<n; i++){
        int key = z[i];
        if(m[key]){
            m[key]++;
        }
        else{
            m[key] = 1;
        }
    }
    vector<PAIR> vpair;

    //把map的值赋给向量
    for(map<int, int>::iterator it=m.begin();it!=m.end();it++)
    {
        vpair.push_back(make_pair(it->first, it->second));
    }

    //给向量排序
    sort(vpair.begin(), vpair.end(), com);
    //输出排好序的向量
    // for_each(vpair.begin(), vpair.end(), outint);
    for(int i = 0; i < vpair.size(); ++i) {
        cout << "For pair " << i << ", the key is: " << vpair[i].first << "; the frequency is: " << vpair[i].second << endl;
    }
    cout << endl;
    return 0;
}
```
