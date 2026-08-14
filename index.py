import numpy as np

# =====================================================================
# PASSO 1: Definição dos Estados e da Matriz de Transição
# =====================================================================

# Lista com os estados possíveis do clima
states = ["Ensolarado", "Nublado", "Chuvoso"]

# Matriz de transição de probabilidades
# Linhas = Estado Atual | Colunas = Próximo Estado
# Linha 0 (Ensolarado): 80% continuar ensolarado, 15% ficar nublado, 5% chover
# Linha 1 (Nublado):    20% ensolarar, 60% continuar nublado, 20% chover
# Linha 2 (Chuvoso):    25% ensolarar, 25% ficar nublado, 50% continuar chovendo
transition_matrix = [
    [0.80, 0.15, 0.05],  # Transições a partir de "Ensolarado"
    [0.20, 0.60, 0.20],  # Transições a partir de "Nublado"
    [0.25, 0.25, 0.50]   # Transições a partir de "Chuvoso"
]

# Configurações da simulação
initial_state = "Ensolarado"  # O clima de hoje (Dia 1)
num_days = 15                # Quantidade de dias que queremos prever


# =====================================================================
# PASSO 2: Implementação da Lógica da Cadeia de Markov
# =====================================================================

def get_state_index(state):
    """Retorna o índice (0, 1 ou 2) do estado atual."""
    return states.index(state)


def predict_weather(initial_state, num_days):
    """Simula a transição de estados dia a dia com base na matriz."""
    current_state = initial_state
    forecast = [current_state]  # Começa a lista com o clima do primeiro dia

    # Gera a previsão para os dias seguintes
    for _ in range(num_days - 1):
        # Encontra a linha referente ao clima de hoje
        current_index = get_state_index(current_state)
        
        # Seleciona o próximo dia de forma aleatória segundo as probabilidades
        next_state = np.random.choice(
            states, 
            p=transition_matrix[current_index]
        )
        
        # Registra o resultado e avança um dia
        forecast.append(next_state)
        current_state = next_state

    return forecast


# =====================================================================
# PASSO 3: Execução e Exibição dos Resultados
# =====================================================================

# Executa a previsão
forecast = predict_weather(initial_state, num_days)

# Exibe o resultado na tela
print(f"--- PREVISÃO DO TEMPO (CADEIA DE MARKOV) ---")
print(f"Estado Inicial: {initial_state}\n")

for day, state in enumerate(forecast, start=1):
    print(f"Dia {day:02d}: {state}")