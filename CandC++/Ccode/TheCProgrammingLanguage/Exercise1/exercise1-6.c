/* ��ϰ 1-6. ��֤���ʽ getchar() != EOF ��ֵ�� 0 ���� 1. */


#include <stdio.h>
main()
{
    int c;
    if ( c = (getchar() != EOF) == 1)
        printf("(getchar() != EOF) = 1");
    else
        printf("(getchar() != EOF) = 0");
    return 0;
}


/*Ҳ�������²������±���c�Ĵ���ʵ��*/

/*
#include <stdio.h>
main()
{
    if ( (getchar() != EOF) == 1)
        printf("The value of \"getchar() != EOF\" is 1.");
    else
        printf("The value of \"getchar() != EOF\" is 0.");
}
*/

/*
�ʼǣ�һ��EOF=ctrl+z�����뻻�к�ctrl+z���С��������������򶼿��Խ��ܶ���ַ�Ϊ���룬����ֻ�е�һ���ַ���Ч��
Ҳ�������һ��������ctrl+z����������������ַ������������0�ˡ�
*/
