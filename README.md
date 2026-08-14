<div align="center">

# Weather Markov Chain Simulator

  <p align="center">
    <strong>Simulador Estocástico de Previsão do Tempo Baseado em Cadeias de Markov</strong>
  </p>

  <!-- BADGES / SHIELDS -->
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3873A9?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
    <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge" alt="Status" />
    <img src="https://img.shields.io/badge/AI%20%26%20Data-Markov%20Chains-FF6F00?style=for-the-badge" alt="Markov Chains" />
  </p>

</div>

---

> [!NOTE]
> **Contexto do Projeto:**  
> Projeto desenvolvido durante o programa **Tech Builder**, focado na implementação prática de **Processos Estocásticos** e **Cadeias de Markov**, aplicando probabilidade condicional para simulação e modelagem temporal de dados climáticos.

---

## 📄 Contexto e Conceito

A **Cadeia de Markov** é um modelo estocástico que descreve uma sequência de eventos onde a probabilidade do próximo estado depende exclusivamente do **estado atual** (Propriedade de Markov / Ausência de Memória).

Neste projeto, o modelo prevê a evolução diária do clima alternando entre 3 estados possíveis:
* ☀️ **Ensolarado**
* ☁️ **Nublado**
* 🌧️ **Chuvoso**

A transição diária é guiada por uma **Matriz de Transição Estocástica** $P$, onde cada elemento $P_{i,j}$ representa a probabilidade de transitar do estado $i$ para o estado $j$.

---

## 📊 Matriz de Transição de Probabilidades

A dinâmica das transições climáticas do modelo é regida pela seguinte distribuição condicional:

| Estado Atual ($t$) \ Próximo Estado ($t+1$) | Ensolarado | Nublado | Chuvoso |
| :--- | :---: | :---: | :---: |
| **Ensolarado** | $80\%$ | $15\%$ | $5\%$ |
| **Nublado** | $20\%$ | $60\%$ | $20\%$ |
| **Chuvoso** | $25\%$ | $25\%$ | $50\%$ |

> **Validação Estocástica:**  
> A soma das probabilidades de cada linha da matriz é igual a $1.0$ ($100\%$), respeitando o axioma de distribuição de probabilidade.

---

## ⚙️ Arquitetura e Funcionamento do Código

A simulação é executada em Python utilizando a biblioteca **NumPy** para sorteio estocástico vetorial:

1. **Mapeamento de Estados:** Indexação dos estados discretos para consulta rápida na matriz.
2. **Amostragem Aleatória Ponderada (`np.random.choice`):** A cada iteração do loop, o próximo estado do clima é escolhido respeitando o vetor de probabilidades da linha referente ao clima do dia atual.
3. **Propagação Temporal:** O estado escolhido torna-se a nova referência para a transição do dia seguinte.

---

## 💻 Instruções de Execução

### Pré-requisitos
* Python 3.8+ instalado.
* Biblioteca `numpy` instalada.

```bash
# Instalação das dependências
pip install numpy
```

### Executando no Terminal

```bash
# 1. Clone o repositório
git clone [https://github.com/SEU_USUARIO/NuvemDeMarkov.git](https://github.com/SEU_USUARIO/NuvemDeMarkov.git)

# 2. Acesse a pasta do projeto
cd NuvemDeMarkov

# 3. Execute o script principal
python index.py
```

---

## 📈 Saída Esperada no Terminal

```text
--- PREVISÃO DO TEMPO (CADEIA DE MARKOV) ---
Estado Inicial: Ensolarado

Dia 01: Ensolarado
Dia 02: Nublado
Dia 03: Nublado
Dia 04: Nublado
Dia 05: Nublado
Dia 06: Nublado
Dia 07: Ensolarado
Dia 08: Ensolarado
Dia 09: Nublado
Dia 10: Nublado
Dia 11: Ensolarado
Dia 12: Ensolarado
Dia 13: Ensolarado
Dia 14: Ensolarado
Dia 15: Ensolarado
```

---

<div align="center">
  <p>Desenvolvido por <strong>João Victor Sitta</strong> durante o programa <strong>Tech Builder</strong> 🚀</p>
</div>
