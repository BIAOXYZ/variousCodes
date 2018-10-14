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
