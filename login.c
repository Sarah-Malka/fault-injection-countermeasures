#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#define PASSWORD "5127bhcsbjh6473829"

__attribute__((noreturn, noinline)) void enterpage()
{
    while (true);
}

void userlogin(char* password)
{
    login(password);
}
void managerlogin(char* password)
{
    login(password);
}
void login(char* password)
{
    for (int i = 0; i < strlen(password); ++i)
    {
        if (password[i] != PASSWORD[i])
        {
            return;
        }
    }
    enterpage();
}
int main()
{
    int number = 0;
    char* password = "5127bhcsbjh6473829";
    if (number == 0)
    {
        return -1;
    }
    if (number == 1)
    {
        userlogin(password);
    }
    if (number == 2)
    {
        managerlogin(password);
    }
    return 0;
}