#include <stdio.h>
#define MAXLINE 1000    /* 最大输入行长度 */

int getline(char line[], int max);
int strindex(char source[], char searchfor[]);

char pattern[] = "ould";    /* 待查找的模式 */

/* 找出所有与模式相匹配的行 */
main()
{
    char line[MAXLINE];
    int found = 0;

    while (getline(line, MAXLINE) > 0)
        if (strindex(line, pattern) >= 0) {
            printf("%s", line);
            found++;
        }
    return found;
}
