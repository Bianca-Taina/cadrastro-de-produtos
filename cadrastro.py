def formatar_nome(nome):
    return nome.strip().title()

def cadrastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    categoria = input("Digite a categoria do produto: ")
    return (formatar_nome(nome), preco, categoria)

def salvar_produto(produto):
    with open("produtos.txt", "a", encoding="utf-8") as arquivo:
        linha = f"{produto[0]};{produto[1]};{produto[2]}\n"
        arquivo.write(linha)

def listar_produtos():
    try:
        with open("produtos,txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome

        