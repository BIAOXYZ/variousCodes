/* ��ϰ 1-9. дһ�����򣬽����뿽������������ҽ������������Ķ���ո��滻Ϊ�����ո�*/


/*
˼·�������ǿո�ֱ�������������OUTSPACE״̬�������ո��������ۡ�
1.һ�������ǿո񣬾������������ǿո���ַ���������OUTSPACE״̬��
2.�������OUTSPACE״̬�������ո�Ҳ���Ǵ��ַ�������ĵ�һ���ո񣩣����������ո�
  ͬʱ��ʾ������һ��INSPACE��״̬��
3.�������INSPACE״̬�������ո�Ҳ���������ǵڶ����ո��ˣ�����ʲôҲ������
*/

// /*
#include <stdio.h>

# define OUTSPACE 0
# define INSPACE 1

int main()
{
    int c;
    int state = OUTSPACE; // �������ĳ�INSPACE�����������������ڵ�һ���ǿո��ַ�֮ǰ���ֵ����Կո��޷���ʾ��Ҳ���ǲ����ܳ��ֿո��ڿ�ͷ��һ���Ƿǿո�ͷ��

    while ( (c = getchar()) != EOF ){
        if (c != ' '){
            putchar(c);
            state = OUTSPACE;
        }
        else if (c == ' ' && state == OUTSPACE){
            putchar(c);
            state = INSPACE;
        }
        else if (c == ' ' && state == INSPACE){
            ;
        }
    }
    return 0;
}
// */

/* �򻯰�������£�д��ʱ�����ʶ���ˣ���������еڶ���else if��ȫ���࣬
��Ϊ�Ǹ���֧���������κ����顣*/

/*
#include <stdio.h>

# define OUTSPACE 0
# define INSPACE 1

int main()
{
    int c;
    int state = OUTSPACE;

    while ( (c = getchar()) != EOF ){
        if (c != ' '){
            putchar(c);
            state = OUTSPACE;
        }
        else if (c == ' ' && state == OUTSPACE){
            putchar(c);
            state = INSPACE;
        }
    }
    return 0;
}
*/

/*���򻯰�*/

/*
#include <stdio.h>

# define OUTSPACE 0
# define INSPACE 1

int main()
{
    int c;
    int state = OUTSPACE;

    while ( (c = getchar()) != EOF ){
        if (c != ' '){
            putchar(c);
            state = OUTSPACE;
        }
        else if (state == OUTSPACE){    //��������"else"ǧ�����١�����ڶ���if�͵�һ��if�ɲ��еĹ�ϵ�ˡ���������һ��a�������aa��
            putchar(c);
            state = INSPACE;
        }
    }
    return 0;
}
*/
