#if 0

/* 下面的原始计算器程序（其仅适用于支票簿核算）中给出了这个声明。
程序按行每次读入一个数（每行一个数，数的前面可能带有正负号），
并将这些数加在一起，并在每次输入之后将当前的总和打印出来：*/

#include <stdio.h>

#define MAXLINE 100

/* 原始计算器 */
main()
{
    double sum, atof(char []);
    char line[MAXLINE];
    int getline(char line[], int max);

    sum = 0;
    while (getline(line, MAXLINE) > 0)
        printf("\t%g\n", sum += atof(line));
    return 0;
}

#endif // 0



/* 下面的原始计算器程序（其仅适用于支票簿核算）中给出了这个声明。
程序按行每次读入一个数（每行一个数，数的前面可能带有正负号），
并将这些数加在一起，并在每次输入之后将当前的总和打印出来：*/

#include <stdio.h>

#define MAXLINE 100

/* 原始计算器 */
main()
{
    double sum, atof(char []);
    char line[MAXLINE];
    int getline(char line[], int max);

    sum = 0;
    while (getline(line, MAXLINE) > 0)
        printf("\t%g\n", sum += atof(line));
    return 0;
}
