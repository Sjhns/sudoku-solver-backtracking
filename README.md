# 🧩 Sudoku Solver (Backtracking)

Este projeto implementa um **resolvedor de Sudoku** utilizando o algoritmo de **backtracking** — uma técnica clássica de busca e retrocesso usada para explorar todas as possibilidades até encontrar uma solução válida.


## 🎯 Objetivo
Preencher um tabuleiro 9×9 de Sudoku com números de **1 a 9** de forma que:
- Cada **linha** contenha todos os números de 1 a 9 sem repetição;
- Cada **coluna** contenha todos os números de 1 a 9 sem repetição;
- Cada **bloco 3×3** contenha todos os números de 1 a 9 sem repetição.


## ⚙️ Funcionamento do Algoritmo

O algoritmo segue os seguintes passos:

1. **Encontrar uma célula vazia** (representada por `0`).
2. **Tentar preencher** essa célula com um número de 1 a 9.
3. **Verificar se é válido** (não viola nenhuma regra do Sudoku).
4. Se for válido, **prosseguir recursivamente** para a próxima célula vazia.
5. Caso não exista número possível, **retroceder (backtrack)** e tentar outro valor.
6. Quando não restarem células vazias, o Sudoku está resolvido.

## 🧮 Invariante, Correção e Terminação

- **Invariante:** a cada chamada recursiva, o tabuleiro parcial sempre respeita as regras do Sudoku.  
- **Correção:** o algoritmo testa todas as combinações válidas — se houver solução, ela será encontrada.  
- **Terminação:** como o número de células vazias é finito, o algoritmo sempre termina (profundidade ≤ 81).


## ⏱️ Complexidade
| Tipo | Descrição |
|------|------------|
| **Tempo (pior caso)** | O(9^k), onde *k* é o número de células vazias |
| **Espaço** | O(k) devido à profundidade da recursão |


## 🧠 Otimizações possíveis
- **MRV (Minimum Remaining Values):** escolher primeiro a célula com menos possibilidades válidas.  
- **Forward Checking:** eliminar valores impossíveis antes de tentar.  
- **Bitmasks ou arrays booleanos:** checar restrições em O(1).  
- **Ordem heurística:** tentar valores menos restritivos primeiro.

## 💻 Exemplo de uso

```python
from sudoku_solver import resolver_sudoku, print_sudoku

sudoku = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

print("Sudoku inicial:")
print_sudoku(sudoku)

if resolver_sudoku(sudoku):
    print("Sudoku resolvido:")
    print_sudoku(sudoku)
else:
    print("Sem solução possível.")
