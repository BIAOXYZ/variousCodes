/* ��ϰ 1-13. дһ�����򣬴�ӡ�����е��ʳ��ȵ�ֱ��ͼ��ˮƽ�����ֱ��ͼ�Ƚ����ף���ֱ��
���ֱ��ͼ�����Ѷȡ� */

/*
˼·��
ˮƽ����ֱ��ͼ��
1.����һ����20��Ԫ�ص�����WordLen[20]��Ҳ��������������뵥�ʳ���Ϊ20���ٶ���Ҳû��ϵ�����Ǹĸ������±���£���
2.ÿһ������Ԫ��WordLen[i]�洢����Ϊi+1�ĵ��ʵĸ�����
3.Ȼ���ӡʱ��ǰ������Ԫ�ص��ڼ����ʹ�ӡ����С���顣
��ֱ����ֱ��ͼ��
*/

/* ������һ��ASCII�뿴���ĸ��Ǻ�ɫС���顣
�Ӷ��û�ֱ��ͼ���������û�У������ñ�ģ�271�����档 */

/*�����õ�271���������϶��õ���219����������219���������ƺ���
�����롣����һ��ԭ���ǿ���̨��Ĭ�ϴ���ҳѡ������⡣
����μ����http://zhidao.baidu.com/question/120270750.html��*/


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

/* histogram �Ӻ���*/

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
