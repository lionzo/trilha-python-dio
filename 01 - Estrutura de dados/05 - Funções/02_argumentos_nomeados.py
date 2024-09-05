def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # Pode acontecer de enviar valores trocados
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # Resolve o problema acima, mas tem problemas se os argumentos tiverem os nomes alterados
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # *args => Os valores vem em uma tupla; **kwargs => Valores vem em um dicionário
