#include <stdlib.h>

#include "tahoot.h"

int main(void) {
    Question* qu = get_next_question((uint8_t)2003);
    if (qu == NULL) {
        perror("get_next_question failed!");
        exit(EXIT_FAILURE);
    }

    printf("%s \n1) %s\n2) %s\n3) %s\n4) %s\n", qu->qu_str, qu->ans_grp[0],
           qu->ans_grp[1], qu->ans_grp[2], qu->ans_grp[3]);

    exit(EXIT_SUCCESS);
}