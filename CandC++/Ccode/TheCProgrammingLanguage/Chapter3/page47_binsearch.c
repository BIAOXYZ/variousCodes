#if 0

������һ�����ֲ��Һ���Ϊ����˵����·�ж����÷����ú����ж������ź�������� v ��
�Ƿ����һ���ض���ֵ x������ v ��Ԫ�ر����Ե����������С���� v �д��� x���������� x
�� v �е�λ�ã����� 0 �� n-1 ֮���һ�����������򷵻� -1��
���ֲ��ҷ����Ƚ�����ֵ x ������ v ���м�Ԫ�ؽ��бȽϡ���� x С���м�ֵ����ô����
���������ǰ�벿�֣������������ĺ�벿�֡����������������һ�����ǽ� x ����ѡ��һ
����м�Ԫ�ؽ��бȽϡ����ֽ����ҷ�Χһ��Ϊ���Ĺ��̻�һֱ�������ҵ�����ֵ���߲��ҷ�
Χ���Ϊֹ��

/* binsearch���� v[0] <= v[1] <= �� <= v[n-1] �в��� x */
int binsearch(int x, int v[], int n)
{
    int low, high, mid;

    low = 0;
    high = n �C 1;
    while (low <= high) {
        mid = (low+high) / 2;
        if (x < v[mid])
            high = mid - 1;
        else if (x > v[mid])
            low = mid + 1;
        else    /* �ҵ�ƥ�� */
            return mid;
    }
    return -1; /* ��ƥ�� */
}

�˳������Ҫ�ж�������ÿһ���� x �Ƿ�С�ڡ����ڻ��ǵ����м�Ԫ�� v[mid]��������
else-if ���ó��Ĺ�����

#endif // 0


/* binsearch���� v[0] <= v[1] <= �� <= v[n-1] �в��� x */
int binsearch(int x, int v[], int n)
{
    int low, high, mid;

    low = 0;
    high = n �C 1;
    while (low <= high) {
        mid = (low+high) / 2;
        if (x < v[mid])
            high = mid - 1;
        else if (x > v[mid])
            low = mid + 1;
        else    /* �ҵ�ƥ�� */
            return mid;
    }
    return -1; /* ��ƥ�� */
}

