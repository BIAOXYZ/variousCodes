#include <stdio.h>
#include <stdlib.h>     /* 为了使用 atof() 函数 */

#define MAXOP 100       /* 操作数或运算符的最大长度 */
#define NUMBER '0'      /* 标示找到一个数 */

int getop(char []);
void push(double);
double pop(void);

/* 逆波兰计算器 */
main()
{
    int type;
    double op2;
    char s[MAXOP];

    while ((type = getop(s)) != EOF) {
        switch (type) {
        case NUMBER:
            push(atof(s));
            break;
        case '+':
            push(pop() + pop());
            break;
        case '*':
            push(pop() * pop());
            break;
        case '-':
            op2 = pop();
            push(pop() - op2);
            break;
        case '/':
            op2 = pop();
            if (op2 != 0.0)
                push(pop() / op2);
            else
                printf("error: 除零溢出\n");
            break;
        case '\n':
            printf("\t%.8g\n", pop());
            break;
        default:
            printf("error: 未知命令 %s\n", s);
            break;
        }
    }
    return 0;
}



#define MAXVAL 100  /* 栈 val 的最大深度 */

int sp = 0;         /* 栈的下一个空闲位置*/
double val[MAXVAL]; /* 存放值的栈 */

/* push：把 f 压入栈中 */
void push(double f)
{
    if (sp < MAXVAL)
        val[sp++] = f;
    else
        printf ("error: 栈满，不能将%g 压栈\n", f);
}

/* pop：弹出并返回栈顶的值 */
double pop(void)
{
    if (sp > 0)
        return val[--sp];
    else {
        printf ("error: 栈空\n");
        return 0.0;
    }
}



#include <ctype.h>

int getch(void);
void ungetch(int);

/* getop：取下一个运算符或数值操作数 */
int getop(char s[])
{
    int i, c;

    while ((s[0] = c = getch()) == ' ' || c == '\t')
        ;
    s[1] = '\0';
    if (!isdigit(c) && c != '.')
        return c; /* 不是数字 */
    i = 0;
    if (isdigit(c)) /* 收集整数部分 */
        while (isdigit(s[++i] = c = getch()))
            ;
    if (c == '.') /* 收集小数部分 */
        while (isdigit(s[++i] = c = getch()))
            ;
    s[i] = '\0';
    if (c != EOF)
        ungetch(c);
    return NUMBER;
}



#define BUFSIZE 100

char buf[BUFSIZE];  /* 供 unget 函数使用的缓冲区 */
int bufp = 0;       /* buf 中的下一个空闲位置 */

int getch(void)     /* 取一个字符（可能是压回的字符） */
{
    return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c) /* 将字符压回到输入中 */
{
    if (bufp >= BUFSIZE)
        printf("ungetch: 压回字符过多\n");
    else
        buf[bufp++] = c;
}


/***************分割线***************/


/* 复制过来整理缩进后的版本，目前已经发现的错误如下：
1. case '-':
        op2 = pop();
        push(pop() – op2);
        break;
减号是中文符号。

2. pop()函数类型应该都是double，但是声明时候是对的。到后面
定义的时候就变成void类型了。
*/

#if 0


#include <stdio.h>
#include <stdlib.h>     /* 为了使用 atof() 函数 */

#define MAXOP 100       /* 操作数或运算符的最大长度 */
#define NUMBER '0'      /* 标示找到一个数 */

int getop(char []);
void push(double);
double pop(void);

/* 逆波兰计算器 */
main()
{
    int type;
    double op2;
    char s[MAXOP];

    while ((type = getop(s)) != EOF) {
        switch (type) {
        case NUMBER:
            push(atof(s));
            break;
        case '+':
            push(pop() + pop());
            break;
        case '*':
            push(pop() * pop());
            break;
        case '-':
            op2 = pop();
            push(pop() – op2);
            break;
        case '/':
            op2 = pop();
            if (op2 != 0.0)
                push(pop() / op2);
            else
                printf("error: 除零溢出\n");
            break;
        case '\n':
            printf("\t%.8g\n", pop());
            break;
        default:
            printf("error: 未知命令 %s\n", s);
            break;
        }
    }
    return 0;
}



#define MAXVAL 100  /* 栈 val 的最大深度 */

int sp = 0;         /* 栈的下一个空闲位置*/
double val[MAXVAL]; /* 存放值的栈 */

/* push：把 f 压入栈中 */
void push(double f)
{
    if (sp < MAXVAL)
        val[sp++] = f;
    else
        printf ("error: 栈满，不能将%g 压栈\n", f);
}

/* pop：弹出并返回栈顶的值 */
void pop(void)
{
    if (sp > 0)
        return val[--sp];
    else {
        printf ("error: 栈空\n");
        return 0.0;
    }
}



#include <ctype.h>

int getch(void);
void ungetch(int);

/* getop：取下一个运算符或数值操作数 */
int getop(char s[])
{
    int i, c;

    while ((s[0] = c = getch()) == ' ' || c == '\t')
        ;
    s[1] = '\0';
    if (!isdigit(c) && c != '.')
        return c; /* 不是数字 */
    i = 0;
    if (isdigit(c)) /* 收集整数部分 */
        while (isdigit(s[++i] = c = getch()))
            ;
    if (c == '.') /* 收集小数部分 */
        while (isdigit(s[++i] = c = getch()))
            ;
    s[i] = '\0';
    if (c != EOF)
        ungetch(c);
    return NUMBER;
}



#define BUFSIZE 100

char buf[BUFSIZE];  /* 供 unget 函数使用的缓冲区 */
int bufp = 0;       /* buf 中的下一个空闲位置 */

int getch(void)     /* 取一个字符（可能是压回的字符） */
{
    return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c) /* 将字符压回到输入中 */
{
    if (bufp >= BUFSIZE)
        printf("ungetch: 压回字符过多\n");
    else
        buf[bufp++] = c;
}


#endif // 0
