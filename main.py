from datetime import datetime


# Definição das estruturas de dados
class Categoria:
    def __init__(self, nome):
        self.nome = nome


class Produto:
    def __init__(self, codigo, nome, categoria, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade


class Movimentacao:
    def __init__(self, produto, tipo, quantidade, data=None):
        self.produto = produto
        self.tipo = tipo  # "entrada" ou "saida"
        self.quantidade = quantidade
        self.data = data if data else datetime.now()


# Estruturas para armazenar dados
categorias = []
produtos = []
movimentacoes = []


# Funções de cadastro
def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome)
    categorias.append(nova_categoria)
    print(f"Categoria '{nome}' cadastrada com sucesso.")


def cadastrar_produto(codigo, nome, categoria_nome, preco, quantidade):
    # Buscar categoria
    categoria = next((c for c in categorias if c.nome == categoria_nome), None)
    if not categoria:
        print(f"Categoria '{categoria_nome}' não encontrada.")
        return

    novo_produto = Produto(codigo, nome, categoria, preco, quantidade)
    produtos.append(novo_produto)
    print(f"Produto '{nome}' cadastrado com sucesso.")


# Funções de consulta
def consultar_produto(codigo):
    produto = next((p for p in produtos if p.codigo == codigo), None)
    if produto:
        print(f"Produto: {produto.nome}, Categoria: {produto.categoria.nome}, Preço: {
              produto.preco}, Quantidade em estoque: {produto.quantidade}")
    else:
        print(f"Produto com código '{codigo}' não encontrado.")


def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    for produto in produtos:
        print(f"Código: {produto.codigo}, Nome: {produto.nome}, Categoria: {
              produto.categoria.nome}, Estoque: {produto.quantidade}")


# Funções de movimentação de estoque
def movimentar_estoque(codigo_produto, tipo, quantidade):
    produto = next((p for p in produtos if p.codigo == codigo_produto), None)
    if not produto:
        print(f"Produto com código '{codigo_produto}' não encontrado.")
        return

    if tipo == "entrada":
        produto.quantidade += quantidade
        print(f"{quantidade} unidades adicionadas ao estoque de '{produto.nome}'.")

    elif tipo == "saida":
        if produto.quantidade >= quantidade:
            produto.quantidade -= quantidade
            print(f"{quantidade} unidades removidas do estoque de '{
                  produto.nome}'.")
        else:
            print(f"Quantidade insuficiente em estoque para realizar a saída.")

    movimentacao = Movimentacao(produto, tipo, quantidade)
    movimentacoes.append(movimentacao)


# Funções de relatório e consulta de movimentações
def gerar_relatorio_estoque():
    print("Relatório de Estoque:")
    for produto in produtos:
        print(f"Produto: {produto.nome}, Estoque: {produto.quantidade}")


def consultar_movimentacoes(codigo_produto):
    produto = next((p for p in produtos if p.codigo == codigo_produto), None)
    if not produto:
        print(f"Produto com código '{codigo_produto}' não encontrado.")
        return

    print(f"Movimentações do produto '{produto.nome}':")
    for mov in movimentacoes:
        if mov.produto.codigo == codigo_produto:
            tipo_mov = "Entrada" if mov.tipo == "entrada" else "Saída"
            print(f"{tipo_mov}: {mov.quantidade} unidades em {
                  mov.data.strftime('%d/%m/%Y %H:%M')}")


# Exemplo de uso do sistema
cadastrar_categoria("Eletrônicos")
cadastrar_categoria("Vestuário")

cadastrar_produto(1, "Smartphone", "Eletrônicos", 2500.00, 80)
cadastrar_produto(2, "Camiseta", "Vestuário", 70.00, 150)

listar_produtos()

movimentar_estoque(1, "entrada", 10)
movimentar_estoque(1, "saida", 5)
movimentar_estoque(2, "saida", 50)

gerar_relatorio_estoque()

consultar_movimentacoes(1)
