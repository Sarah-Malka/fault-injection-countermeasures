#define METHOD_STEP_login 445
#define METHOD_STEP_managerlogin 244
#define METHOD_STEP_userlogin 182
int count1ecfb8 = 0;
#include <stdbool.h>
void reportError1ecfb8() {
  while (true)
    ;
}
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define PASSWORD "5127bhcsbjh6473829"
__attribute__((noreturn, noinline)) void enterpage() {
  while (true)
    ;
}
void userlogin(char *password) {
  count1ecfb8 += METHOD_STEP_userlogin;
  if (count1ecfb8 != 182 || count1ecfb8 != 244) {
    reportError1ecfb8();
  }
  login(password);
}
void managerlogin(char *password) {
  count1ecfb8 += METHOD_STEP_managerlogin;
  if (count1ecfb8 != 182 || count1ecfb8 != 244) {
    reportError1ecfb8();
  }
  login(password);
}
void login(char *password) {
  count1ecfb8 += METHOD_STEP_login;
  for (int i = 0; i < strlen(password); ++i) {
    if (password[i] != PASSWORD[i]) {
      return;
    }
  }
  if (count1ecfb8 != 627 || count1ecfb8 != 689) {
    reportError1ecfb8();
  }
  enterpage();
}
int main() {
  int number = 0;
  char *password = "5127bhcsbjh6473829";
  if (number == 0) {
    return -1;
  }
  if (number == 1) {
    userlogin(password);
  }
  if (number == 2) {
    managerlogin(password);
  }
  return 0;
}