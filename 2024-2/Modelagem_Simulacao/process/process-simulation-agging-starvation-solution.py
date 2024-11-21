import random

# Solicita entradas do usuário
num_processos = int(input("Digite a quantidade de processos: "))
num_processadores = int(input("Digite a quantidade de processadores: "))

# Gera os processos
processos = []
for i in range(1, num_processos + 1):
    quantidade_tarefas = random.randint(0, 250)
    prioridade = random.randint(0, 3)
    processos.append({
        'id': i,
        'tarefas_totais': quantidade_tarefas,
        'tarefas_restantes': quantidade_tarefas,
        'prioridade': prioridade,    # Prioridade base
        'aging_bonus': 0,            # Incremento devido ao aging
        'tempo_espera': 0            # Tempo que o processo espera na fila
    })

# Inicializa os processadores com capacidades individuais
processadores = []
for i in range(1, num_processadores + 1):
    capacidade = int(input(f"Digite a capacidade de processamento por segundo do Processador {i}: "))
    processadores.append({
        'id': i,
        'capacidade': capacidade,
        'disponivel_em': 0,
        'processos_processados': [],
        'tempo_total': 0
    })

# Relatórios iniciais
print("\nRelação de Processadores e suas capacidades:")
for processador in processadores:
    print(f"Processador {processador['id']} - Capacidade: {processador['capacidade']} tarefas/segundo")

print("\nLista de Processos com prioridades e quantidade de tarefas:")
for processo in processos:
    print(f"Processo {processo['id']} - Prioridade: {processo['prioridade']} - Tarefas Totais: {processo['tarefas_totais']}")

# Simula o escalonamento com aging
linha_do_tempo = []
tempo_atual = 0
aging_intervalo = 5  # Intervalo para aumentar prioridade

while any(p['tarefas_restantes'] > 0 for p in processos):
    # Atualiza prioridade efetiva com base no aging
    for processo in processos:
        if processo['tarefas_restantes'] > 0:
            if processo['tempo_espera'] > 0 and processo['tempo_espera'] % aging_intervalo == 0:
                if processo['prioridade'] - processo['aging_bonus'] > 0:
                    processo['aging_bonus'] += 1  # Aumenta o bonus de prioridade
    # Calcula prioridade efetiva
    for processo in processos:
        processo['prioridade_efetiva'] = processo['prioridade'] - processo['aging_bonus']
    # Ordena os processos por prioridade efetiva e tempo de espera
    fila_processos = sorted([p for p in processos if p['tarefas_restantes'] > 0],
                            key=lambda x: (x['prioridade_efetiva'], x['tempo_espera'], x['id']))
    processos_atendidos = set()
    for processador in processadores:
        if processador['disponivel_em'] <= tempo_atual:
            if fila_processos:
                processo = fila_processos.pop(0)
                tarefas_a_processar = min(processo['tarefas_restantes'], processador['capacidade'])
                tempo_de_execucao = 1  # Tempo fixo de execução
                processo['tarefas_restantes'] -= tarefas_a_processar
                processo['tempo_espera'] = 0  # Reseta tempo de espera
                processador['disponivel_em'] = tempo_atual + tempo_de_execucao
                processador['tempo_total'] += tempo_de_execucao
                processador['processos_processados'].append(processo['id'])
                linha_do_tempo.append({
                    'tempo_inicio': tempo_atual,
                    'tempo_fim': processador['disponivel_em'],
                    'processador': processador['id'],
                    'processo': processo['id'],
                    'tarefas_processadas': tarefas_a_processar,
                    'prioridade_base': processo['prioridade'],
                    'prioridade_efetiva': processo['prioridade_efetiva']
                })
                processos_atendidos.add(processo['id'])
    # Incrementa tempo de espera dos processos não atendidos
    for processo in processos:
        if processo['tarefas_restantes'] > 0 and processo['id'] not in processos_atendidos:
            processo['tempo_espera'] += 1
    tempo_atual += 1

# Exibe o relatório detalhado
print("\nLinha do Tempo de Processamento:")
for evento in sorted(linha_do_tempo, key=lambda x: x['tempo_inicio']):
    if evento['prioridade_base'] != evento['prioridade_efetiva']:
        prioridade_info = f"{evento['prioridade_base']} (> {evento['prioridade_efetiva']} devido ao aging)"
    else:
        prioridade_info = f"{evento['prioridade_base']}"
    print(f"De {evento['tempo_inicio']}s a {evento['tempo_fim']}s, Processador {evento['processador']} processou {evento['tarefas_processadas']} tarefas do Processo {evento['processo']} (Prioridade {prioridade_info})")

# Relatório por processador
print("\nRelatório por Processador:")
for processador in processadores:
    processos_unicos = set(processador['processos_processados'])
    print(f"Processador {processador['id']}:")
    print(f" - Processos processados: {', '.join(map(str, processos_unicos))}")
    print(f" - Tempo total de operação: {processador['tempo_total']}s")

# Relatório por processo
print("\nRelatório por Processo:")
processos_dict = {p['id']: p for p in processos}

for processo in processos:
    eventos_processo = [evento for evento in linha_do_tempo if evento['processo'] == processo['id']]
    if eventos_processo:
        tempo_inicio = eventos_processo[0]['tempo_inicio']
        tempo_fim = eventos_processo[-1]['tempo_fim']
        tempo_processamento_total = sum([evento['tempo_fim'] - evento['tempo_inicio'] for evento in eventos_processo])
        processos_dict[processo['id']]['tempo_inicio'] = tempo_inicio
        processos_dict[processo['id']]['tempo_fim'] = tempo_fim
        processos_dict[processo['id']]['tempo_processamento_total'] = tempo_processamento_total
    else:
        processos_dict[processo['id']]['tempo_inicio'] = None
        processos_dict[processo['id']]['tempo_fim'] = None
        processos_dict[processo['id']]['tempo_processamento_total'] = 0

# Ordena processos pela ordem em que começaram a ser processados
processos_ordenados = sorted(processos_dict.values(), key=lambda x: x['tempo_inicio'] if x['tempo_inicio'] is not None else float('inf'))

for processo in processos_ordenados:
    if processo['tempo_inicio'] is not None:
        print(f"Processo {processo['id']} começou em {processo['tempo_inicio']}s, terminou em {processo['tempo_fim']}s, tempo total de processamento: {processo['tempo_processamento_total']}s")
    else:
        print(f"Processo {processo['id']} não foi processado.")