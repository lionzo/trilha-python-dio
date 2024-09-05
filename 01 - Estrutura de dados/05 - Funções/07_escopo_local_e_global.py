salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_bonus(500)  # 2500

def salario_bonus_2 (valor_total,bonus):
    valor_total += bonus
    return valor_total


print(salario_bonus_2(salario, 320))

print(salario)