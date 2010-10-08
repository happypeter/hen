#include <stdio.h>

void readinput(char * ss);
void expand(char * from, char * to);

int main(int argc, const char *argv[])
{
    char s1[10];
    char s2[30];
    readinput(s1);
    printf("s1 is %s\n", s1);
    expand(s1, s2); 
    printf("s2: %s\n",s2);
    return 0;
}

void readinput(char * ss)
{
    int i;
    for(i = 0;i != 10;i++) 
    {
        ss[i] = getchar(); 
        if(ss[i] == '\n') break;
    }
    ss[i] = '\0';

}
void expand(char * from, char * to)
{
    char c;
    int i = 0;
    int j = 0;
    while(1) // skip leading blank
    {
        if(from[i] == ' ')
            i++;
        else
            break;
    }
    if(from[i] == '-') //handle leading '-'
    {
        to[j] = '-';
        j++;
        i++;
    }
    printf("from[i] = %c\n", from[i]);
    printf("from[i+2] = %c\n", from[i+2]);
    for(c = from[i]; c <= from[i+2]; c++) 
    {
        to[j] = c;
        j++;
    }
    if(from[i+3] == '-') // now let's handle "a-b-f-"
    {
        if(from[i+4] == '\0') // then the case is "a-z-"
            to[j++] = '-'; // show '-' as it is 
        else if(isalpha(from[i+4]))
        {
            for(c = from[i+2], c += 1; c <= from[i+4]; c++) 
            // we need c += 1 here, since we do not want "a-c-d" -> "abccd"
            {
                to[j] = c;
                j++;
            }
        }
        else
            printf("OK!\n"); // for gardian: we can use if(isalpha()) then goto err; 
            goto err;        

        if(from[i+5] == '-') // if there is still a trailing '-', show it
        {
            to[j] = '-'; 
            j++;
        }
    }
    else if(isdigit(from[i+3])) // now let's handle "a-b1-9"
    {
        for(c = from[i+3]; c <= from[i+5]; c++) 
        {
            to[j] = c;
            j++;
        }
        if(from[i+6] == '-') // if there is still a trailing '-', show it
        {
            to[j] = '-'; 
            j++;
        }

    }
    else
        printf("done \n");

    to[j] = '\0';
    if(0) // do we really need this ?
    {
        err:
        {
            printf("wrong format\n");
            printf("usage: a-b1-9\n");
            for (i = 0; i <= j ; i++) 
            {
                to[i] = 0;
            }
            return ;
        }
    }
}


