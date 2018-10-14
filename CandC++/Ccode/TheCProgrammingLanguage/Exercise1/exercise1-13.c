/* 练习 1-13. 写一个程序，打印输入中单词长度的直方图。水平方向的直方图比较容易；垂直方
向的直方图更有难度。 */

/*
思路：
水平方向直方图：
1.定义一个有20个元素的数组WordLen[20]，也就是允许最大输入单词长度为20（再多了也没关系，就是改改数组下标的事）。
2.每一个数组元素WordLen[i]存储长度为i+1的单词的个数。
3.然后打印时当前的数组元素等于几，就打印几个小方块。
垂直方向直方图：
*/

/* 测试了一下ASCII码看看哪个是黑色小方块。
从而好画直方图。结果好像没有，决定用别的（271）代替。 */

/*本来用的271，但是网上都用的是219。我试了下219发现是类似汉字
的乱码。后来一查原来是控制台的默认代码页选项的问题。
详情参加这里（http://zhidao.baidu.com/question/120270750.html）*/


#include<stdio.h>

#define MAXWORDLEN 25

void hhistogram(char s1[]);
void vhistogram(char s2[]);

int main()
{
    char choice;

    printf("Please choose the direction of the histogram.\nYou MUST input exactly \"h\" or \"v\" (h=horizontal; v=vertical).\n");
    scanf("%c",&choice);

    if (choice == 'h'){
        printf("The choice is \"%c\". It will display a horizontal histogram.",choice);
    }
    else if (choice == 'v'){
        printf("The choice is \"%c\". It will display a vertical histogram.",choice);
    }
    else
    {
        printf("Sorry, you have only one chance, byebye~");
        return -1;
    }

    return 0;
}

/* histogram 子函数*/

void hhistogram(char s1[])
{
    int c;

    while ( (c = getchar()) != EOF ){
        ;
    }
}

void vhistogram(char s2[])
{
    int c;
}
