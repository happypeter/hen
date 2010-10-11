for (i = 0; i < lim -1; i++) 
{
    c = getchar();
    if (c == '\n') 
    {
        break;  
    }
    else if (c == EOF) 
    {
        break;
    }
    else
        s[i] = c;
}
