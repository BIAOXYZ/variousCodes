#include<bits/stdc++.h>

using namespace std;

//int n;
struct rect{
    //int rectNo;
    int x1, y1, x2, y2;
    //int overlap;
};

int main(){
    int n;
    cin >> n;
    struct rect rect[n];

    for(int i=0; i< n; i++){
        cin >> rect[i].x1 >> rect[i].y1 >> rect[i].x2 >> rect[i].y2;
    }

    // int area;  -->  不初始化的话有问题
    int area = 0;
    int flag[101][101];

    // ������ʼ��
    //memset(flag, false, sizeof(flag));
    for(int i=0; i< n; i++){

        //�����������ص��������
        area += (rect[i].x2 - rect[i].x1) * (rect[i].y2 - rect[i].y1);

        for(int j=rect[i].x1; j<rect[i].x2; j++){
            for(int t=rect[i].y1; t<rect[i].y2; t++){
                if(flag[j][t] == 1){
                    area--;

                }
                else{
                flag[j][t] = 1;
                }
            }
        }
    }

    cout << area <<endl;;
}

/*
3019795	画图	03-21 18:16	962B	CPP11	错误	40	15ms	3.082MB
*/
