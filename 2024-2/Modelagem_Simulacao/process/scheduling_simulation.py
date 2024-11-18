import random

# Classe que representa um processador
class Processador:
    def __init__(self, id, taxa_processamento):
        self.id = id
        self.taxa_processamento = taxa_processamento
        self.tempo_atual = 0
        self.tarefas_processadas = 0
        self.processos_processados = 0

    def processar(self, tarefa, tempo_atual):
        tempo_inicio = max(self.tempo_atual, tempo_atual)
        tempo_processamento = tarefa.quantidade_processos / self.taxa_processamento
        self.tempo_atual = tempo_inicio + tempo_processamento
        self.tarefas_processadas += 1
        self.processos_processados += tarefa.quantidade_processos
        tarefa.tempo_restante = 0
        return (
            tarefa.id,
            self.id,
            tempo_inicio,
            self.tempo_atual,
            tarefa.quantidade_processos,
            tarefa.prioridade,
        )

# Classe que representa um processador para Round Robin
class ProcessadorRR:
    def __init__(self, id, taxa_processamento):
        self.id = id
        self.taxa_processamento = taxa_processamento
        self.tarefas_processadas = 0
        self.processos_processados = 0

    def processar(self, tarefa, tempo_atual, quantum):
        capacidade_processamento = self.taxa_processamento * quantum
        processos_executados = min(tarefa.tempo_restante, capacidade_processamento)
        tempo_processamento = processos_executados / self.taxa_processamento
        tarefa.tempo_restante -= processos_executados
        self.processos_processados += processos_executados
        return (
            tarefa.id,
            self.id,
            tempo_atual,
            tempo_atual + tempo_processamento,
            processos_executados,
            tarefa.prioridade,
            tarefa.tempo_restante,
        )

# Classe que representa uma tarefa
class Tarefa:
    def __init__(self, id, quantidade_processos, prioridade):
        self.id = id
        self.quantidade_processos = quantidade_processos
        self.prioridade = prioridade
        self.tempo_restante = quantidade_processos

# Classe que representa a simulação
class Simulacao:
    def __init__(self, processadores, logica, quantum=None):
        self.processadores = processadores
        self.fila_tarefas = []
        self.historico = []
        self.linha_do_tempo = []
        self.tempo_total = 0
        self.logica = logica
        self.quantum = quantum

    def adicionar_tarefa(self, tarefa):
        self.fila_tarefas.append(tarefa)

    def preparar_fila(self):
        if self.logica == 1:  # FIFO
            pass  # A fila já está na ordem de chegada
        elif self.logica == 2:  # Prioridade
            self.fila_tarefas.sort(key=lambda t: t.prioridade)
        elif self.logica == 3:  # SJF
            self.fila_tarefas.sort(key=lambda t: t.quantidade_processos)

    def executar(self):
        tempo_atual = 0
        if self.logica == 4:  # Round Robin
            fila_rr = self.fila_tarefas.copy()
            while fila_rr:
                for processador in self.processadores:
                    if not fila_rr:
                        break
                    tarefa = fila_rr.pop(0)
                    detalhes = processador.processar(tarefa, tempo_atual, self.quantum)
                    self.historico.append(detalhes)
                    self.linha_do_tempo.append(
                        f"Processador {detalhes[1]} processou Tarefa {detalhes[0]} "
                        f"(Prioridade {detalhes[5]}) de {detalhes[2]:.2f} a {detalhes[3]:.2f} segundos, "
                        f"Processos executados: {int(detalhes[4])}, Processos restantes: {int(detalhes[6])}"
                    )
                    if tarefa.tempo_restante > 0:
                        fila_rr.append(tarefa)
                tempo_atual += self.quantum
            self.tempo_total = tempo_atual
        else:
            self.preparar_fila()
            for tarefa in self.fila_tarefas:
                processador = min(self.processadores, key=lambda p: p.tempo_atual)
                detalhes = processador.processar(tarefa, processador.tempo_atual)
                self.historico.append(detalhes)
                self.linha_do_tempo.append(
                    f"Processador {detalhes[1]} processou Tarefa {detalhes[0]} "
                    f"(Prioridade {detalhes[5]}) de {detalhes[2]:.2f} a {detalhes[3]:.2f} segundos"
                )
            self.tempo_total = max(p.tempo_atual for p in self.processadores)

    def gerar_relatorio(self):
        print("\nLógica de Escalonamento Utilizada:")
        if self.logica == 1:
            print("FIFO (First In, First Out): As tarefas são processadas na ordem de chegada.")
        elif self.logica == 2:
            print("Prioridade: As tarefas são processadas de acordo com a prioridade (menor valor tem maior prioridade).")
        elif self.logica == 3:
            print("SJF (Shortest Job First): As tarefas com menor quantidade de processos são processadas primeiro.")
        elif self.logica == 4:
            print(f"Round Robin: As tarefas são processadas em ordem cíclica com quantum de {self.quantum} segundos.")
        else:
            print("Lógica desconhecida.")

        print("\nRelatório de Processamento:")
        for detalhes in self.historico:
            if self.logica == 4:
                print(
                    f"Tarefa {detalhes[0]} (Prioridade {detalhes[5]}) processada pelo Processador {detalhes[1]} "
                    f"de {detalhes[2]:.2f} a {detalhes[3]:.2f} segundos, "
                    f"Processos executados: {int(detalhes[4])}, Processos restantes: {int(detalhes[6])}"
                )
            else:
                print(
                    f"Tarefa {detalhes[0]} (Prioridade {detalhes[5]}) processada pelo Processador {detalhes[1]} "
                    f"de {detalhes[2]:.2f} a {detalhes[3]:.2f} segundos "
                    f"com quantidade de processos {int(detalhes[4])}"
                )
        print(f"\nTempo total decorrido: {self.tempo_total:.2f} segundos")

        print("\nLinha do Tempo de Processos:")
        for evento in self.linha_do_tempo:
            print(evento)

def main():
    print("Selecione a lógica de escalonamento:")
    print("1. FIFO")
    print("2. Prioridade")
    print("3. SJF")
    print("4. Round Robin")
    logica = int(input("Digite o número da lógica desejada: "))
    quantum = None

    if logica == 4:
        quantum = float(input("Digite o valor do quantum para Round Robin: "))
        num_processadores = int(input("Digite o número de processadores: "))
        processadores = []
        for i in range(num_processadores):
            id = i + 1
            taxa_processamento = float(input(f"Digite a taxa de processamento do processador {id} (processos por segundo): "))
            processadores.append(ProcessadorRR(id, taxa_processamento))
    else:
        num_processadores = int(input("Digite o número de processadores: "))
        processadores = []
        for i in range(num_processadores):
            id = i + 1
            taxa_processamento = float(input(f"Digite a taxa de processamento do processador {id} (processos por segundo): "))
            processadores.append(Processador(id, taxa_processamento))

    simulacao = Simulacao(processadores, logica, quantum)
    num_tarefas = int(input("Digite o número de tarefas: "))
    for i in range(num_tarefas):
        id = i + 1
        quantidade_processos = random.randint(1, 100)  # Limite até 100 processos por tarefa
        prioridade = random.randint(1, 5)
        simulacao.adicionar_tarefa(Tarefa(id, quantidade_processos, prioridade))

    simulacao.executar()
    simulacao.gerar_relatorio()

if __name__ == "__main__":
    main()