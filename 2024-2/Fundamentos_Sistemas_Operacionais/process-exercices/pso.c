#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

// Exercício 1: Criação de Processos
// Este programa demonstra a criação de processos usando fork() e exibe os PIDs dos processos pai e filho.

int main() {
    pid_t procID;

    // Cria um novo processo
    procID = fork();

    if (procID < 0) {
        printf("Erro na criação do novo processo\n");
        return -1;
    } else if (procID == 0) {
        // Processo Filho
        printf("Processo filho - para o FILHO o fork devolveu %d\n", procID);
        printf("Processo filho - PID = %d\n", getpid());
        return 1;
    } else {
        // Processo Pai
        printf("Processo Pai - para o PAI o fork devolveu %d\n", procID);
        printf("Processo Pai - PID = %d\n", getpid());
        return 1;
    }
}

/*
Explicação:
- O comando fork() cria um novo processo.
- Para o processo pai, fork() retorna o PID do processo filho.
- Para o processo filho, fork() retorna 0.
- Em caso de erro, fork() retorna -1.
*/

#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

// Exercício 2: Espera por Processo
// Este programa demonstra o uso de wait() para esperar a conclusão de um processo filho.

int f1(int x) {
    printf("x = %d\n", x);
    return 0;
}

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
        f1(100);
        printf("Filho executou a função f1 do Pai...\n");
        return 1;
    } else {
        // Processo Pai
        wait(NULL); // Espera o filho terminar
        printf("Processo Pai - PID = %d\n", getpid());
        f1(50);
        printf("Pai executou a função f1...\n");
        return 1;
    }
}

/*
Explicação:
- O processo pai cria um processo filho usando fork().
- O processo pai espera o término do processo filho usando wait().
- O processo filho executa a função f1() com o argumento 100.
- O processo pai executa a função f1() com o argumento 50 após o término do filho.
*/

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

#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

// Exercício 4: Quantidade de Processos Criados
// Este programa demonstra a criação de múltiplos processos usando fork().

int main() {
    fork();
    fork();
    printf("PID = %d\n", getpid());
    return 1;
}

/*
Explicação:
- O primeiro fork() cria um novo processo, totalizando 2 processos.
- O segundo fork() é executado por ambos os processos, criando mais 2 processos, totalizando 4 processos.
- Cada processo imprime seu PID.
*/

#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

// Exercício 5: Espaço de Endereçamento de Processos
// Este programa demonstra que cada processo tem seu próprio espaço de endereçamento.

int s = 0;

int main() {
    if (fork() == 0) {
        // Processo Filho
        s = 10;
        printf("Processo filho, s = %d\n", s);
    } else {
        // Processo Pai
        wait(NULL); // Espera o filho terminar
        printf("Filho terminou a execução!\n");
        printf("Processo pai, s = %d\n", s);
    }
    return 0;
}

/*
Explicação:
- O processo filho altera o valor da variável s para 10.
- O processo pai espera o término do processo filho usando wait().
- O processo pai imprime o valor da variável s, que permanece 0.
- Cada processo tem seu próprio espaço de endereçamento, então as alterações feitas pelo filho não afetam o pai.
*/