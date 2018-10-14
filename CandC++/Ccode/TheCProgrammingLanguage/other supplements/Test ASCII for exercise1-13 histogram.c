/* 测试了一下ASCII码看看哪个是黑色小方块。
从而好画直方图。结果好像没有，决定用别的（271）代替。 */

/*本来用的271，但是网上都用的是219。我试了下219发现是类似汉字
的乱码。后来一查原来是控制台的默认代码页选项的问题。
详情参加这里（http://zhidao.baidu.com/question/120270750.html）*/

#include<stdio.h>

main()
{
    int i;
    for (i=1; i<= 500; i++)
    printf("%d--%c  ",i,i);

    printf("\n");
    int j;
    for (j=1; j<= 10; j++)
    //printf("%c",271);
    printf("%c",219);

    return 0;
}
