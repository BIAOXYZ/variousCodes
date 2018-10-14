#include <stdio.h>
#include <stdlib.h>     /* Ϊ��ʹ�� atof() ���� */

#define MAXOP 100       /* �����������������󳤶� */
#define NUMBER '0'      /* ��ʾ�ҵ�һ���� */

int getop(char []);
void push(double);
double pop(void);

/* �沨�������� */
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
                printf("error: �������\n");
            break;
        case '\n':
            printf("\t%.8g\n", pop());
            break;
        default:
            printf("error: δ֪���� %s\n", s);
            break;
        }
    }
    return 0;
}



#define MAXVAL 100  /* ջ val �������� */

int sp = 0;         /* ջ����һ������λ��*/
double val[MAXVAL]; /* ���ֵ��ջ */

/* push���� f ѹ��ջ�� */
void push(double f)
{
    if (sp < MAXVAL)
        val[sp++] = f;
    else
        printf ("error: ջ�������ܽ�%g ѹջ\n", f);
}

/* pop������������ջ����ֵ */
double pop(void)
{
    if (sp > 0)
        return val[--sp];
    else {
        printf ("error: ջ��\n");
        return 0.0;
    }
}



#include <ctype.h>

int getch(void);
void ungetch(int);

/* getop��ȡ��һ�����������ֵ������ */
int getop(char s[])
{
    int i, c;

    while ((s[0] = c = getch()) == ' ' || c == '\t')
        ;
    s[1] = '\0';
    if (!isdigit(c) && c != '.')
        return c; /* �������� */
    i = 0;
    if (isdigit(c)) /* �ռ��������� */
        while (isdigit(s[++i] = c = getch()))
            ;
    if (c == '.') /* �ռ�С������ */
        while (isdigit(s[++i] = c = getch()))
            ;
    s[i] = '\0';
    if (c != EOF)
        ungetch(c);
    return NUMBER;
}



#define BUFSIZE 100

char buf[BUFSIZE];  /* �� unget ����ʹ�õĻ����� */
int bufp = 0;       /* buf �е���һ������λ�� */

int getch(void)     /* ȡһ���ַ���������ѹ�ص��ַ��� */
{
    return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c) /* ���ַ�ѹ�ص������� */
{
    if (bufp >= BUFSIZE)
        printf("ungetch: ѹ���ַ�����\n");
    else
        buf[bufp++] = c;
}


/***************�ָ���***************/


/* ���ƹ�������������İ汾��Ŀǰ�Ѿ����ֵĴ������£�
1. case '-':
        op2 = pop();
        push(pop() �C op2);
        break;
���������ķ��š�

2. pop()��������Ӧ�ö���double����������ʱ���ǶԵġ�������
�����ʱ��ͱ��void�����ˡ�
*/

#if 0


#include <stdio.h>
#include <stdlib.h>     /* Ϊ��ʹ�� atof() ���� */

#define MAXOP 100       /* �����������������󳤶� */
#define NUMBER '0'      /* ��ʾ�ҵ�һ���� */

int getop(char []);
void push(double);
double pop(void);

/* �沨�������� */
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
            push(pop() �C op2);
            break;
        case '/':
            op2 = pop();
            if (op2 != 0.0)
                push(pop() / op2);
            else
                printf("error: �������\n");
            break;
        case '\n':
            printf("\t%.8g\n", pop());
            break;
        default:
            printf("error: δ֪���� %s\n", s);
            break;
        }
    }
    return 0;
}



#define MAXVAL 100  /* ջ val �������� */

int sp = 0;         /* ջ����һ������λ��*/
double val[MAXVAL]; /* ���ֵ��ջ */

/* push���� f ѹ��ջ�� */
void push(double f)
{
    if (sp < MAXVAL)
        val[sp++] = f;
    else
        printf ("error: ջ�������ܽ�%g ѹջ\n", f);
}

/* pop������������ջ����ֵ */
void pop(void)
{
    if (sp > 0)
        return val[--sp];
    else {
        printf ("error: ջ��\n");
        return 0.0;
    }
}



#include <ctype.h>

int getch(void);
void ungetch(int);

/* getop��ȡ��һ�����������ֵ������ */
int getop(char s[])
{
    int i, c;

    while ((s[0] = c = getch()) == ' ' || c == '\t')
        ;
    s[1] = '\0';
    if (!isdigit(c) && c != '.')
        return c; /* �������� */
    i = 0;
    if (isdigit(c)) /* �ռ��������� */
        while (isdigit(s[++i] = c = getch()))
            ;
    if (c == '.') /* �ռ�С������ */
        while (isdigit(s[++i] = c = getch()))
            ;
    s[i] = '\0';
    if (c != EOF)
        ungetch(c);
    return NUMBER;
}



#define BUFSIZE 100

char buf[BUFSIZE];  /* �� unget ����ʹ�õĻ����� */
int bufp = 0;       /* buf �е���һ������λ�� */

int getch(void)     /* ȡһ���ַ���������ѹ�ص��ַ��� */
{
    return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c) /* ���ַ�ѹ�ص������� */
{
    if (bufp >= BUFSIZE)
        printf("ungetch: ѹ���ַ�����\n");
    else
        buf[bufp++] = c;
}


#endif // 0
