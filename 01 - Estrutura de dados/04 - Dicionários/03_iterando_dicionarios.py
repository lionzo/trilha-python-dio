# contatos = {
#     "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
#     "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
#     "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
#     "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
# }

# for chave in contatos:
#     print(chave, contatos[chave])

# print("=" * 100)

# for chave, valor in contatos.items():
#     print(chave, valor)

# produtos = ["Notebook", "Mouse", "Teclado", "Mouse", "Monitor", "Mouse", "Teclado"]
# contagem = {}
# max_count = 0
# max_produto = None
# for produto in produtos:
#         if produto in contagem:
#             contagem[produto] += 1
#         else:
#             contagem[produto] = 1
# for produto, count in contagem.items():
#     if count > max_count:
#           max_count = count
#           max_produto = produto
# print(max_produto, max_count)

def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    for produto, count in contagem.items():
        # TODO: Encontre o produto com a maior contagem:
      if count > max_count:
        max_count = count
        max_produto = produto    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    produtos = entrada.split(',')
    produtos = [produto.strip() for produto in produtos]
    return produtos

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))