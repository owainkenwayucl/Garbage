#include <stdio.h>
#include <string.h>

void dothing(char *arg) {
  printf("String: \"%s\", length: %lu\n", arg, strlen(arg));
}

int main(void)
{
  char *thing;
  thing="hi";
  dothing(thing);
}
