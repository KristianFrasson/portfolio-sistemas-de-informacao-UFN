#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

// Exercício 1: Programa com dois processos (área e perímetro)
// Este programa calcula a área e o perímetro de um terreno retangular utilizando dois processos, um para cada cálculo.

int main() {
    float largura, comprimento;

    // Entrada de dados do terreno
    printf("Informe a largura do terreno: ");
    scanf("%f", &largura);
    printf("Informe o comprimento do terreno: ");
    scanf("%f", &comprimento);

    // Cria o processo filho
    pid_t pid = fork();

    if (pid == 0) { 
        // Processo Filho - Calcula a área
        float area = largura * comprimento;
        printf("Filho: A área do terreno é: %.2f\n", area);
    } else {
        // Processo Pai - Calcula o perímetro
        wait(NULL); // Espera o filho terminar
        float perimetro = 2 * (largura + comprimento);
        printf("Pai: O perímetro do terreno é: %.2f\n", perimetro);
    }

    return 0;
}

/*
Explicação:
- O processo pai calcula o perímetro do terreno.
- O processo filho calcula a área do terreno.
- O comando fork() é usado para criar um processo filho.
*/

#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

// Exercício 2: Programa com 3 processos concorrentes
// Três processos executam um laço de repetição e imprimem suas identificações, permitindo observar o escalonamento de processos.

int main() {
    int N;

    // Entrada do número de interações
    printf("Informe o número de interações: ");
    scanf("%d", &N);

    // Criação de três processos
    for (int i = 0; i < 3; i++) {
        if (fork() == 0) {
            for (int j = 0; j < N; j++) {
                printf("Processo %d: Iteração %d\n", getpid(), j + 1);
                sleep(1); // Pause para visualizar o escalonamento
            }
            return 0;
        }
    }

    // Processo pai aguarda todos os filhos
    for (int i = 0; i < 3; i++) {
        wait(NULL);
    }

    return 0;
}

/*
Explicação:
- Cada processo imprime sua ID e o número da iteração.
- O comportamento do escalonamento pode ser observado pela ordem em que os processos imprimem suas saídas.
*/

#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

// Exercício 3: Processo pai e dois filhos com intervalos de tempo
// Este programa cria um processo pai e dois processos filhos, cada um imprimindo números em diferentes intervalos.

void filho1() {
    for (int i = 100; i <= 200; i++) {
        printf("Filho1: %d\n", i);
        sleep(1);
    }
    printf("Filho1 finalizou.\n");
}

void filho2() {
    for (int i = 250; i <= 350; i++) {
        printf("Filho2: %d\n", i);
        sleep(1);
    }
    printf("Filho2 finalizou.\n");
}

void pai() {
    for (int i = 1; i <= 50; i++) {
        printf("Pai: %d\n", i);
        sleep(2);
    }
    printf("Pai finalizou.\n");
}

// Função principal
int main() {
    pid_t pid1 = fork();

    if (pid1 == 0) {
        filho1();
    } else {
        pid_t pid2 = fork();
        if (pid2 == 0) {
            filho2();
        } else {
            pai();
            wait(NULL);  // Espera pelos filhos
            wait(NULL);
        }
    }

    return 0;
}

/*
Explicação:
- O processo pai imprime números de 1 a 50 com intervalos de 2 segundos.
- O filho1 imprime de 100 a 200 e o filho2 de 250 a 350, ambos com intervalos de 1 segundo.
*/

#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

// Exercício 4: Árvore de processos
// Este programa cria uma árvore de processos com um pai e cinco filhos.

int main() {
    pid_t filho1, filho2, filho3, filho4, filho5;

    filho1 = fork();
    if (filho1 == 0) {
        printf("Filho 1 criado\n");
        filho4 = fork();
        if (filho4 == 0) {
            printf("Filho 4 criado\n");
            return 0;
        }
        wait(NULL); // Filho 1 espera Filho 4
        return 0;
    }

    filho2 = fork();
    if (filho2 == 0) {
        printf("Filho 2 criado\n");
        filho5 = fork();
        if (filho5 == 0) {
            printf("Filho 5 criado\n");
            return 0;
        }
        wait(NULL); // Filho 2 espera Filho 5
        return 0;
    }

    filho3 = fork();
    if (filho3 == 0) {
        printf("Filho 3 criado\n");
        return 0;
    }

    // Processo pai espera todos os filhos
    wait(NULL);
    wait(NULL);
    wait(NULL);

    printf("Processo Pai finalizou\n");
    return 0;
}

/*
Explicação:
- O processo pai cria três filhos.
- O filho 1 e o filho 2 criam mais um filho cada um, formando uma árvore de processos.
*/