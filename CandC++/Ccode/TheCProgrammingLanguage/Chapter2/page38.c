#if 0

/* ��׼�������һ������ֲ��α������������Լ�һ�����ڳ�ʼ�������ӵĺ�����ǰ�߸���
��һ��ǿ��ת����ʾ����*/

unsigned long int next = 1;

/* rand������һ��α�����������ֵ��Ϊ 0..32767 */
int rand(void)
{
    next = next * 1103515245 + 12345;
    return (unsigned int)(next/65536) % 32768;
}

/* srand��Ϊ rand()�������� */
void srand(unsigned int seed)
{
    next = seed;
}

#endif


unsigned long int next = 1;

/* rand������һ��α�����������ֵ��Ϊ 0..32767 */
int rand(void)
{
    next = next * 1103515245 + 12345;
    return (unsigned int)(next/65536) % 32768;
}

/* srand��Ϊ rand()�������� */
void srand(unsigned int seed)
{
    next = seed;
}
