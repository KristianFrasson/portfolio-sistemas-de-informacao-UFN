#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>


void signal_handler(int signal_number) {
    if (signal_number == SIGINT) {
        printf("\nRecebido SIGINT (Ctrl+C). Encerrando o programa...\n");
        exit(0);
    } else if (signal_number == SIGTERM) {
        printf("\nRecebido SIGTERM. Encerrando o programa...\n");
        exit(0);
    }
}

int main() {

    if (signal(SIGINT, signal_handler) == SIG_ERR) {
        perror("Não foi possível configurar o manipulador para SIGINT");
        exit(1);
    }

    if (signal(SIGTERM, signal_handler) == SIG_ERR) {
        perror("Não foi possível configurar o manipulador para SIGTERM");
        exit(1);
    }

    printf("Programa em execução. Pressione Ctrl+C para interromper ou envie SIGTERM para terminar.\n");


    while (1) {

        sleep(1);
    }

    return 0;
}
