/* ��ϰ 1-7. дһ�����򣬽� EOF ��ֵ��ӡ������*/

// /*
#include <stdio.h>

main()
{
    /* ����֮������4������5������Ϊ��while��"c = getchar()"����Ѿ���ִ��һ���ˡ�����ʹ�ò�������ʵ�顣
    �����5�Ļ����ᷢ����������"1�س�2�س�3�س�4�س�5�س�6�س�"�Ż���ʾ�����������Զ����ء�*/
    int upperRunTime = 4;

    int realRunTime = 1;
    int c;

    while ( (c = getchar()) != EOF )
    {
        if (realRunTime <= upperRunTime)
        {
            c = getchar();
            realRunTime++;
        }
        else
        {
            printf("Poor guy! You've tried more than 5 times. Please stop!");
            return 0;  //�������Թ���"break;"����"exit(0);"�����ƺ�����̫�á�
        }
    }

    printf("The value of EOF is %d", c);

    return 0;
}

// */

/* �ڶ�������Ƚϼ򵥣������ƿ��Գ��ԵĴ����� */

/*
#include <stdio.h>

main()
{
    int c;

    while ( (c=getchar()) != EOF )
    {
        c=getchar();
    }
    printf("EOF=%d",c);
}
*/

/*������������ϣ�http://bbs.chinaunix.net/thread-836784-1-1.html�������ӡ�
�ɼ�EOF�Ѿ������壬����ֱ���á�*/

/*
#include <stdio.h>
int main(int argc,char *argv[])
{
        printf("%d\n",EOF);
        return 0;
}
*/
