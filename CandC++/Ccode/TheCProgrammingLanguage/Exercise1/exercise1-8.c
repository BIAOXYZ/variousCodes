/* 练习 1-8. 写一个程序，统计输入中的空格、制表符和换行符的个数。*/

#include <stdio.h>

int main()
{
    int nSpace, nTab, nLine;
    nSpace = nTab = nLine = 0;
    // int nSpace = nTab = nLine = 0;
    /* 不能直接用"int nSpace = nTab = nLine = 0;"这句，无论是声明还是赋值都不可以！
    第一句直接用这个语句来声明并初始化，会提示nTab和nLine还没声明呢就直接赋值了。
    第一句先声明那三个变量，再用这句赋值吧，又会说nSpace重复声明了（就因为nSpace前面的int，编译器会认为你是在声明）。*/
    int c;

    while ( (c = getchar()) != EOF ){
        if (c == ' ')
            nSpace++;
        else if (c == '\t')
            nTab++;
        else if (c == '\n')
            nLine++;
    }
    printf("The number of spaces, tabs and lines are:\n\tSpace = %d, Tab = %d, Line = %d", nSpace, nTab, nLine);
    return 0;
}
