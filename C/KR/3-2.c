#include <stdio.h>

int escape(char *, char *);
char * reverse(char * );

char to[20];
char from[20];

int main(int argc, const char *argv[])
{
    int k = 0;
/*
 *
 * EOF = -1 and it is a integer, 
 * but 
 * print("%d", (char)c);
 * still ouput -1
 * so the following works as expected
 */
    printf("Plz input the string:\n");
    while((from[k++] = getchar()) != EOF)
        ;
    from[k-1] = '\0';
    escape(from, to); 
    printf("\n\nmake '\\n' and '\\t' visible: %s\n", to);
    printf("now turn it back: \n%s\n", reverse(to));
    return 0;
}


/*
 * this make '\n' and '\t' into "\n" and "\t"
 */
int escape(char * s, char * t)
{
    int j = 0;
    int i;
    for(i=0; s[i]!='\0'; i++)
    {
        char p = s[i];
        switch(p) 
        {
            case '\t':
                t[j++] = '\\';
                t[j++] = 't';
                break;
            case '\n':
                t[j++] = '\\';
                t[j++] = 'n';
                break;
            default:
                t[j++] = s[i]; 
        }       
    t[j] = '\0';

    }

}

/* 
 * this turn "\n" and "\t" back into '\n' and '\t'
 */
char * reverse(char * s)
{
    int i;
    int j = 0;
    for(i = 0; s[i] != '\0'; i++)
    {
        if(s[i] == '\\')
        {

            switch(s[++i])
            {
                case 'n':
                    s[i] = '\n';
                    break;
                case 't':
                    s[i] = '\t';
                    break;
                default:
                    break;
            }

        }
        from[j++] = s[i];
    }
    from[j] = '\0';
    return from;
}
