/*
 * adder.c - a minimal CGI program that adds two numbers together
 */
/* $begin adder */
#include "csapp.h"

int main(void)
{
    char *buf, *p;
    char arg1[MAXLINE], arg2[MAXLINE], content[MAXLINE];
    int n1 = 0, n2 = 0;

    /* Extract the two arguments */
    if ((buf = getenv("QUERY_STRING")) != NULL)
    {
        p = strchr(buf, '&');
        *p = '\0';
        /* original tiny */
        strcpy(arg1, buf);
        strcpy(arg2, p+1);
        n1 = atoi(arg1);
        n2 = atoi(arg2);
        /* ex11.10 adder.html */
        // sscanf(buf, "n1=%d", &n1);
        // sscanf(p+1, "n2=%d", &n2);
    }
    /* ex11.11 HTTP HEAD method */
    char *method = getenv("REQUEST_METHOD");

    /* Make the response body */
    sprintf(content, "QUERY_STRING=%s", buf);
    sprintf(content, "Welcome to add.com: ");
    sprintf(content, "%sTHE Internet addition portal. \r\n<p>", content);
    // sprintf(content, "%sexercise 11.10 done\r\n<p>", content); // ex11.10
    sprintf(content, "%sexercise 11.11 done\r\n<p>", content); // ex11.11
    sprintf(content, "%sThe answer is %d + %d = %d\r\n<p>", content, n1, n2, n1+n2);
    sprintf(content, "%sThanks for visiting!\r\n", content);

    /* Genrat the HTTP response */
    printf("Connections: close\r\n");
    printf("Content-length: %d\r\n", (int)strlen(content));
    printf("Content-type: text/html\r\n\r\n");
    printf("%s", content);
    /* ex11.11 HTTP HEAD method */
    if (strcasecmp(method, "HEAD") != 0)
        printf("%s", content);
    fflush(stdout);

    exit(0);
}
/* $end adder */
