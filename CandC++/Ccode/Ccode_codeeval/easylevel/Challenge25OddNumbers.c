/* https://www.codeeval.com/open_challenges/25/ */
/* ODD NUMBERS */
/* Print the odd numbers from 1 to 99. */

#include<stdio.h>

main()
{
    int oddNum;
    int UPPERBOUND = 99;
    for (oddNum = 1; oddNum <= UPPERBOUND; oddNum+=2)
        printf("%d\n",oddNum);
    return 0;
}
