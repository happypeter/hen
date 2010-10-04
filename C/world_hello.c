#include <stdio.h>
#include <string.h>

char b[200];
char *swap (char a[])
{   int i;
    int j = 0;
    for(i = 0; a[i] != ' '; i++)
        ;
    i++;
    while(b[j++] = a[i++]) 
        ;
    b[--j] = ' ';
    j++;
    for(i = 0; a[i] != ' '; b[j++] = a[i++])
        ;
    printf("b = %s\n", b);
    return b;
}

int main(int argc, const char *argv[])
{
    char a[100];
    int len, i = 0;
    printf("input character:\n");
    while( (a[i++] = getchar()) != '\n')
        ;
    a[i-1] = '\0';

    printf("output string:\n");
   
    printf("%s\n", swap(a));
    return 0;
}
