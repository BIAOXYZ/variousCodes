#include <stdio.h>

#define MAXLINE 1000    /* 允许的输入行最大长度 */

int max;                /* 当前最长输入行长度 */
char line[MAXLINE];     /* 当前输入行 */
char longest[MAXLINE];  /* 当前最长输入行 */

int getline(void);
void copy(void);

/* 打印当前最长输入行，特殊版本 */
main()
{
    int len;
    extern int max;
    extern char longest[];

    max = 0;
    while ((len = getline()) > 0)
        if (len > max) {
            max = len;
            copy();
        }
    if (max > 0)    /* there was a line */
        printf("%s", longest);
    return 0;
}

/* getline：特殊版本 */
int getline(void)
{
    int c, i;
    extern char line[];

    for (i = 0; i < MAXLINE - 1
        && (c=getchar()) != EOF && c != '\n'; ++i)
            line[i] = c;
    if (c == '\n') {
        line[i] = c;
        ++i;
    }
    line[i] = '\0';
    return i;
}

/* copy: 特殊版本 */
void copy(void)
{
    int i;
    extern char line[], longest[];

    i = 0;
    while ((longest[i] = line[i]) != '\0')
        ++i;
}


/* ~~~~~~~~~~分割线~~~~~~~~~~ */
/* 中文版书籍中getline子函数里for循环那段少了个括号 */
/* 因为原本的程序中"星号+正斜杠"类型的注释比较多，
所以只得引入了条件编译*/

/*
原版程序
注意getline子函数里这句

for (i = 0; i < MAXLINE - 1
    && (c=getchar)) != EOF && c != '\n'; ++i)

因为左边两个括号，右边三个括号，所以编译都无法通过。我当时第一反应这么改的：

for (i = 0; i < MAXLINE - 1
    && ((c=getchar)) != EOF && c != '\n'; ++i)

就是在"&&"后面随手加了个左括号，这样两边括号数目是匹配了，调试也弹出命令行了。
但是无法输入任何值。。。想想也正常啊，getchar后面要有一对括号的。不过我就是奇
怪这样也能调得通- -
*/

/* (http://segmentfault.com/q/1010000000449167) */

#if 0

#include <stdio.h>

#define MAXLINE 1000    /* 允许的输入行最大长度 */

int max;                /* 当前最长输入行长度 */
char line[MAXLINE];     /* 当前输入行 */
char longest[MAXLINE];  /* 当前最长输入行 */

int getline(void);
void copy(void);

/* 打印当前最长输入行，特殊版本 */
main()
{
    int len;
    extern int max;
    extern char longest[];

    max = 0;
    while ((len = getline()) > 0)
        if (len > max) {
            max = len;
            copy();
        }
    if (max > 0)    /* there was a line */
        printf("%s", longest);
    return 0;
}

/* getline：特殊版本 */
int getline(void)
{
    int c, i;
    extern char line[];

    for (i = 0; i < MAXLINE - 1
        && (c=getchar)) != EOF && c != '\n'; ++i)
            line[i] = c;
    if (c == '\n') {
        line[i] = c;
        ++i;
    }
    line[i] = '\0';
    return i;
}

/* copy: 特殊版本 */
void copy(void)
{
    int i;
    extern char line[], longest[];

    i = 0;
    while ((longest[i] = line[i]) != '\0')
        ++i;
}

#endif


/*第一次随手一改的结果：能通过编译，并弹出cmd界面，但是无法输入任何值。*/

#if 0

#include <stdio.h>

#define MAXLINE 1000    /* 允许的输入行最大长度 */

int max;                /* 当前最长输入行长度 */
char line[MAXLINE];     /* 当前输入行 */
char longest[MAXLINE];  /* 当前最长输入行 */

int getline(void);
void copy(void);

/* 打印当前最长输入行，特殊版本 */
main()
{
    int len;
    extern int max;
    extern char longest[];

    max = 0;
    while ((len = getline()) > 0)
        if (len > max) {
            max = len;
            copy();
        }
    if (max > 0)    /* there was a line */
        printf("%s", longest);
    return 0;
}

/* getline：特殊版本 */
int getline(void)
{
    int c, i;
    extern char line[];

    for (i = 0; i < MAXLINE - 1
        && ((c=getchar)) != EOF && c != '\n'; ++i)
            line[i] = c;
    if (c == '\n') {
        line[i] = c;
        ++i;
    }
    line[i] = '\0';
    return i;
}

/* copy: 特殊版本 */
void copy(void)
{
    int i;
    extern char line[], longest[];

    i = 0;
    while ((longest[i] = line[i]) != '\0')
        ++i;
}

#endif

