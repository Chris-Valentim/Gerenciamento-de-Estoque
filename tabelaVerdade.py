# Definindo as variáveis booleanas como combinações possíveis
combinacoes = [
    {'P': True, 'E': True, 'L': True, 'R': True},
    {'P': True, 'E': True, 'L': True, 'R': False},
    {'P': True, 'E': True, 'L': False, 'R': True},
    {'P': True, 'E': True, 'L': False, 'R': False},
    {'P': True, 'E': False, 'L': True, 'R': True},
    {'P': True, 'E': False, 'L': True, 'R': False},
    {'P': True, 'E': False, 'L': False, 'R': True},
    {'P': True, 'E': False, 'L': False, 'R': False},
    {'P': False, 'E': True, 'L': True, 'R': True},
    {'P': False, 'E': True, 'L': True, 'R': False},
    {'P': False, 'E': True, 'L': False, 'R': True},
    {'P': False, 'E': True, 'L': False, 'R': False},
    {'P': False, 'E': False, 'L': True, 'R': True},
    {'P': False, 'E': False, 'L': True, 'R': False},
    {'P': False, 'E': False, 'L': False, 'R': True},
    {'P': False, 'E': False, 'L': False, 'R': False}
]


# Função para verificar se a solução completa é atendida
def verificar_solucao(p, e, l, r):
    return p and e and l and r


# Gerando e exibindo a tabela verdade
print("P\tE\tL\tR\tSolução Completa")
for combinacao in combinacoes:
    p = combinacao['P']
    e = combinacao['E']
    l = combinacao['L']
    r = combinacao['R']
    solucao_completa = verificar_solucao(p, e, l, r)
    print(f"{p}\t{e}\t{l}\t{r}\t{solucao_completa}")
