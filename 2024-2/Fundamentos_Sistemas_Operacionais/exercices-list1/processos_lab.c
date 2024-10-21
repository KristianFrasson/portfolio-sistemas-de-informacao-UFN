// Exercício 1
// Valores de PID:
// Para o processo pai, fork devolve o PID do processo filho.
// Para o processo filho, fork devolve 0.
// Finalidade das chamadas ao sistema:
// fork(): Cria um novo processo (processo filho).
// getpid(): Retorna o PID do processo atual.

#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main() {
    pid_t procID;

    procID = fork();

    if (procID < 0) {
        printf("Erro na criação do novo processo\n");
        return -1;
    } else if (procID == 0) {
        printf("Processo filho - para o FILHO o fork devolveu %d\n", procID);
        printf("Processo filho - PID = %d\n", getpid());
        return 1;
    } else {
        printf("Processo Pai - para o PAI o fork devolveu %d\n", procID);
        printf("Processo Pai - PID = %d\n", getpid());
        return 1;
    }
}

// Exercício 2
// O processo pai cria um processo filho.
// O processo pai espera o término do processo filho (wait(NULL)).
// O processo filho executa a função f1 com o argumento 100.
// Após o término do processo filho, o processo pai executa a função f1 com o argumento 50.

int f1(int x) {
    printf("x = %d\n", x);
    return 0;
}

int main() {
    pid_t procID;
    procID = fork();

    if (procID < 0) {
        printf("Erro na criação do novo processo\n");
        return -1;
    } else if (procID == 0) {
        printf("Processo filho - PID = %d\n", getpid());
        f1(100);
        printf("Filho executou a função f1 do Pai...\n");
        return 1;
    } else {
        wait(NULL);
        printf("Processo Pai - PID = %d\n", getpid());
        f1(50);
        printf("Pai executou a função f1...\n");
        return 1;
    }
}

// Exercício 3
// Chamadas ao sistema utilizadas:
// fork(): Cria um novo processo (processo filho).
// execl(): Substitui o código do processo filho pelo código de outro programa.
// exit(): Termina o processo filho.
// wait(NULL): O processo pai espera o término do processo filho.
// Verificação da execução:
// Comentando exit(0): O processo filho continuará executando as instruções seguintes, incluindo printf e sleep.
// Comentando wait(NULL): O processo pai não esperará o término do processo filho e poderá terminar antes do filho.
// Teste da função execl para outro código existente:
// Modifique o argumento de execl para apontar para outro programa executável.

int main() {
    pid_t procID;
    procID = fork();

    if (procID < 0) {
        printf("Erro na criação do novo processo\n");
        return -1;
    } else if (procID == 0) {
        printf("Processo3.c: Processo filho - PID = %d\n", getpid());
        execl("./processo2", "0", "0", NULL);
        exit(0);
        printf("Processo3.c: Filho executou o programa \"processo2.c!\"...\n");
        sleep(3);
    } else {
        wait(NULL);
        printf("Processo3.c: Processo Pai - PID = %d\n", getpid());
        return 1;
    }
}

// Exercício 4
// Quantos processos são criados?
// Inicialmente, há 1 processo.
// O primeiro fork() cria 1 novo processo, totalizando 2 processos.
// O segundo fork() é executado por ambos os processos, criando 2 novos processos, totalizando 4 processos.
// Justificativa:
// Cada chamada a fork() duplica o número de processos em execução.

int main() {
    fork();
    fork();

    printf("PID = %d\n", getpid());

    return 1;
}

// Exercício 5
// Valor da variável s em cada processo:
// No processo filho, s é definido como 10.
// No processo pai, s permanece 0.
// Os processos ocupam o mesmo espaço de endereçamento?
// Não, cada processo tem seu próprio espaço de endereçamento. 
//A variável s é copiada para o processo filho, mas as alterações feitas pelo filho não afetam o pai.

int s = 0;

int main() {
    if (fork() == 0) {
        s = 10;
        printf("Processo filho, s = %d\n", s);
    } else {
        wait(NULL);
        printf("Filho terminou a execução!\n");
        printf("Processo pai, s = %d\n", s);
    }

    return 0;
}