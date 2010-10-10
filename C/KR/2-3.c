#include <stdio.h>

int htoi(char *s);
char input[20];
char *readstring();
int power(int base, int n);

int main(int argc, const char *argv[])
{
    printf("output: 0x%x\n", (htoi(readstring())));
    return 0;
}
char *readstring()
{
    int i = 0;
    while((input[i++] = getchar()) != '\n')
        ; 
    input[i-1] = '\0';
    printf("%s\n", input);
    return input;
    
}
int power(int base, int n)
{
    int result = 1;
    while (n-->0) 
    {
        result *= base;
    }
    return result;
}

int htoi(char *s)
{
    int i = 0;
    int output = 0;
    while(isblank(s[i]))
        i++;
 
    printf("i = %d\n", i);

    if((s[i] == '0') && ((s[i+1] == 'x') || s[i+1] == 'X'))
    {
        i += 2;
    }
    printf("+++s[%d] = %c\n", i, s[i]);
    if(isdigit(s[i]) || (('a' <= s[i]) && (s[i] <= 'f')) || (('A' <= s[i]) && (s[i] <= 'F')))
    {
        printf("tttt\n");   
        int b = strlen(s) - i; // how many significant bits
        int output = 0;
        int bit; // s[bit]
        int value; // the decimal value of s[bit]
        while (b  > 0) 
        {
            bit = strlen(s) - b; // start at i: the first digit bit
            if(s[bit] >= '0' && s[bit] <= '9')
                value = s[bit] - 48 ; 
            else if(s[bit] >= 'a' && s[bit] <= 'f')
                value = s[bit] - 87 ; // 'a' == 97
            else if(s[bit] >= 'A' && s[bit] <= 'F')
                value = s[bit] - 55 ; // 'A' == 65
            else
            {
                printf("wrong...%s\n", &s[i]); // catch "0xa a"
                goto err;
            }
            output += value * power(16, (b - 1));
            printf("NOW: s[%d] = %d \t%d\n", bit, value, power(16, (b - 1)));
            b--;
            printf("111\n");
        }
        printf("222\n");
        return output;
    }
    else
    {
        err:
        printf("wrong input: %s\n", s);
        return -1;
    }

}
