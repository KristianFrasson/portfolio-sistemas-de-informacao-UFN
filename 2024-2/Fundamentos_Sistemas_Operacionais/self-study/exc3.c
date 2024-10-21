#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

// Exercício 3: Chamada de Programas
// Este programa demonstra o uso de execl() para executar um novo programa no processo filho.

int main() {
    pid_t procID;

    // Cria um novo processo
    procID = fork();

    if (procID < 0) {
        printf("Erro na criação do novo processo\n");
        return -1;
    } else if (procID == 0) {
        // Processo Filho
        printf("Processo filho - PID = %d\n", getpid());
        // Descomente uma das linhas abaixo para executar um programa diferente
        // execl("./procTwo", (char *)NULL);
        // execl("/bin/ls", "ls", "-l", (char *)NULL);
        // execl("/bin/ps", "ps", "-aux", (char *)NULL);
        exit(0);
    } else {
        // Processo Pai
        printf("Processo Pai - PID = %d\n", getpid());
        return 0;
    }
}

/*
Explicação:
- O processo filho pode executar um novo programa usando execl().
- O primeiro argumento de execl() é o caminho para o programa a ser executado.
- Os argumentos seguintes são os argumentos passados para o programa.
- O processo pai continua sua execução normalmente.
*/