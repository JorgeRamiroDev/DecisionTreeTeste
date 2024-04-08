
import pulp as pl

# Cria o problema de maximização
model = pl.LpProblem("Maximizar_Lucro", pl.LpMaximize)

# Define as variáveis de decisão
A = pl.LpVariable("Produto_A", lowBound=0, cat='Continuous')
B = pl.LpVariable("Produto_B", lowBound=0, cat='Continuous')

# Adiciona a função objetivo
model += 20 * A + 30 * B, "Lucro_Total"

# Adiciona as restrições
model += A + 3 * B <= 50, "Restricao_Maquina_X"
model += 2 * A + B <= 40, "Restricao_Maquina_Y"

# Resolve o problema
model.solve()

# Mostra os resultados
print("Status:", pl.LpStatus[model.status])
print("Produzir de Produto A:", pl.value(A))
print("Produzir de Produto B:", pl.value(B))
print("Lucro Máximo:", pl.value(model.objective))
