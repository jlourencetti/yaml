input = [
    { "name": "Maria Neusa de Aparecida", "cpf": "97905796671",
    "state": "Sao Paulo", "value": "1234"},
    {"name": "Ricardo Fontes", "cpf": "44010762900",
    "state": "Rio Grande do Sui", "value": "567"}
]


def solucao(arg):
    for v in arg:
        resultado = " ".join(v.values())
        print(resultado)


solucao(input)       