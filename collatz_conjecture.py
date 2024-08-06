import matplotlib.pyplot as plt
import networkx as nx

def collatz_conjecture(n):
  steps = 0
  sequence = [n]

  while n != 1:
    n = n / 2 if n % 2 == 0 else (n * 3) + 1
    sequence.append(n)
    steps += 1
  
  return steps, sequence


def plot_histogram(sequence):
  steps = list(range(1, len(sequence) + 1))
  
  plt.figure(figsize=(10, 5))
  plt.bar(steps, sequence, color='blue')
  plt.xlabel('Etapas')
  plt.ylabel('Valores')
  plt.title('Histograma dos Valores por Etapa na Conjectura de Collatz')
  plt.show()

def plot_line_chart(sequence):
  steps = list(range(1, len(sequence) + 1))
  
  plt.figure(figsize=(10, 5))
  plt.plot(steps, sequence, marker='o', linestyle='-', color='blue')
  plt.xlabel('Etapas')
  plt.ylabel('Valores')
  plt.title('Gráfico de Linhas dos Valores por Etapa na Conjectura de Collatz')
  plt.show()

def plot_directed_graph(sequence):
  G = nx.DiGraph()  # Cria um gráfico direcionado

  # Adiciona nós e arestas ao gráfico
  for i in range(len(sequence) - 1):
    G.add_edge(sequence[i], sequence[i + 1])

  pos = nx.spring_layout(G, seed=50)  # Define o layout dos nós
  plt.figure(figsize=(15, 5))
  nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', arrows=True, font_size=12, font_weight='bold', arrowstyle='-|>', arrowsize=15)
  plt.title('Gráfico Direcionado da Conjectura de Collatz')
  plt.show()

n = int(input('Seleciona um número positivo diferente de 1: '))
steps, sequence = collatz_conjecture(n)
plot_line_chart(sequence)
plot_histogram(sequence)
plot_directed_graph(sequence)
