# Fundamentos de Sistemas Operacionais

## Estudo Dirigido

### Capítulo 2 – Estruturas do Computador ou Estruturas de Sistemas de Computação

**Bibliografia:**
- SILBERSCHATZ, Abraham; GALVIN, Peter; GAGNE, Greg. *Sistemas Operacionais: com Java*. Rio de Janeiro: Elsevier, 2004.
- DEITEL, H. M. et al. *Sistemas operacionais*. 3. ed. São Paulo, SP: Pearson, 2005. E-book. Disponível em: [Plataforma Virtual](https://plataforma.bvirtual.com.br/Leitor/Loader/315/epub/0?keep=False)

### Questões

1. **Caracterize um sistema de computação moderno:**
   Um sistema de computação moderno é composto por hardware, software e firmware. O hardware inclui componentes físicos como CPU, memória, dispositivos de entrada/saída e armazenamento. O software inclui o sistema operacional e aplicativos que gerenciam os recursos do hardware e executam tarefas específicas. O firmware é um software embutido em hardware que fornece controle de baixo nível para os dispositivos.

2. **Quais são as etapas de inicialização do computador?**
   - **Power-On Self Test (POST):** Verificação inicial do hardware.
   - **Carregamento do Bootloader:** O BIOS/UEFI carrega o bootloader na memória.
   - **Carregamento do Sistema Operacional:** O bootloader carrega o kernel do sistema operacional.
   - **Inicialização do Kernel:** O kernel inicializa os drivers e serviços essenciais.
   - **Inicialização dos Serviços e Aplicativos:** O sistema operacional carrega serviços e aplicativos de inicialização.

3. **O que é interrupção? Como os Sistemas Operacionais tratam as interrupções?**
   Interrupção é um sinal enviado ao processador indicando que um evento requer atenção imediata. Os sistemas operacionais tratam interrupções através de rotinas de tratamento de interrupções (ISR), que pausam a execução do processo atual, salvam seu estado, executam a ISR e depois retomam a execução do processo interrompido.

4. **Defina I/O síncrona e I/O assíncrona. Qual permite melhor uso da CPU?**
   - **I/O Síncrona:** O processo espera a conclusão da operação de I/O antes de continuar.
   - **I/O Assíncrona:** O processo continua a execução enquanto a operação de I/O é realizada em paralelo.
   - **Melhor uso da CPU:** I/O assíncrona permite melhor uso da CPU, pois não bloqueia o processo durante operações de I/O.

5. **Qual a finalidade da DMA – Direct Memory Access?**
   DMA permite que dispositivos de I/O transfiram dados diretamente para a memória sem intervenção da CPU, liberando a CPU para outras tarefas e aumentando a eficiência do sistema.

6. **Como funciona a RAM? Qual o ciclo básico de execução de uma instrução?**
   A RAM (Memória de Acesso Aleatório) armazena dados e instruções temporariamente para acesso rápido pela CPU. O ciclo básico de execução de uma instrução inclui:
   1. **Busca (Fetch):** A CPU busca a instrução da memória.
   2. **Decodificação (Decode):** A CPU decodifica a instrução.
   3. **Execução (Execute):** A CPU executa a instrução.
   4. **Escrita (Write-back):** A CPU escreve o resultado de volta na memória, se necessário.

7. **Caracterize a estrutura de armazenamento de um sistema de computação:**
   A estrutura de armazenamento inclui:
   - **Memória Primária:** RAM e cache, usadas para armazenamento temporário e rápido acesso.
   - **Memória Secundária:** Discos rígidos, SSDs, usados para armazenamento permanente.
   - **Memória Terciária:** Dispositivos de armazenamento removíveis, como CDs, DVDs e fitas magnéticas.

8. **Em que consiste o uso de cache?**
   O cache é uma memória de alta velocidade que armazena dados frequentemente acessados para reduzir o tempo de acesso à memória principal. Ele melhora o desempenho do sistema ao minimizar o tempo de espera da CPU para acessar dados.

9. **Caracterize os diferentes tipos de proteção de hardware suportados em um sistema de computação:**
   - **Proteção de Memória:** Impede que processos acessem áreas de memória que não lhes pertencem.
   - **Proteção de CPU:** Usa modos de operação (usuário e kernel) para proteger o acesso a instruções privilegiadas.
   - **Proteção de I/O:** Controla o acesso aos dispositivos de I/O para evitar conflitos e uso indevido.
   - **Proteção de Arquivos:** Controla o acesso a arquivos e diretórios para garantir a integridade e segurança dos dados.

### Exemplo com Fork

16. **Exemplo com Fork**
    ```c
    int main(){
        fork();
        fork();
        return 0;
    }
    ```

16.a) **Quantos processos existem?**
    A chamada ao `fork()` duplica o processo. Como há dois `fork()` no código, o número total de processos será 4 (processo original + 3 processos filhos).

16.b) **Qual a hierarquia dos processos?**
    O processo original cria um filho no primeiro `fork()`. Ambos os processos (pai e filho) executam o segundo `fork()`, resultando em mais dois filhos. Portanto, há uma hierarquia de um processo pai e três processos filhos.