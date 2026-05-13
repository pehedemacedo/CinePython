print("     ================================")
print("        Bem Vindo ao CinePython!!!   ")
print("     ================================")

filmes18 = ["O Poderoso Chefão", "Pulp Fiction", "O Senhor dos Anéis", "Matrix", "Clube da Luta"]
idadeMinima18: int = 18
filmesMenores = ["Toy Story", "Frozen", "Procurando Nemo", "Shrek", "Meu Malvado Favorito"]
idadeMinimaMenores = 0

print("")
name = input("Escreva seu Nome: ")
print("Aoba, " + name + "!")
idade = int(input("Insira sua idade: "))
print("Você tem " + str(idade) + " anos!")
print("")
print("================================")
print("")

print("Aqui estão os filmes disponíveis para maiores de " + str(idadeMinima18) + " anos:")
print(filmes18)
print("")
print("================================")
print("")

print("Aqui estão os filmes disponíveis para menores de " + str(idadeMinimaMenores) + " anos:")
print(filmesMenores)
print("")
print("================================")
print("")

filmeEscolhido = input("Qual filme você gostaria de assistir? ")

if(filmeEscolhido in filmes18):
    print("O filme " + filmeEscolhido + " é recomendado para maiores de " + str(idadeMinima18) + " anos.")
    if(idade >= idadeMinima18):
        print("Você tem idade suficiente para assistir " + filmeEscolhido)
    else:
        print("Desculpe, você não tem idade suficiente para assistir " + filmeEscolhido + ".")
elif(filmeEscolhido in filmesMenores):
    print("O filme escolhido foi " + filmeEscolhido)
else:
    print("Desculpe, o filme " + filmeEscolhido + " não está disponível em nosso catálogo.")

print("")
print("================================")
print("Perfeito! Agora vamos escolher a poltrona para assistir " + filmeEscolhido + ".")
print("================================")
print("")

poltronas = 70
poltronasJaEscolhidas = []
poltronasNaoEscolhidas = [
    "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10",
    "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10",
    "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10",
    "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10",
    "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10",
    "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10",
    "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10"
]

poltronasDisponiveis = [p for p in poltronasNaoEscolhidas if p not in poltronasJaEscolhidas]

if(poltronas > 0):
    print("Há ", poltronas, " poltronas disponíveis para o filme " + filmeEscolhido + ".")
    print("Poltronas disponíveis: " + str(poltronasDisponiveis))
    poltronaEscolhida = input("Escolha uma poltrona (a1-a10 - g1-g10): ")
    poltronasJaEscolhidas.append(poltronaEscolhida)
    poltronas -= 1
    print("Poltrona " + poltronaEscolhida + " escolhida. Aproveite o filme!")
    if(poltronaEscolhida in poltronasJaEscolhidas):
        print("Desculpe, a poltrona " + poltronaEscolhida + " já foi escolhida. Por favor, escolha outra poltrona.")
    else:
        print("Poltrona " + poltronaEscolhida + " confirmada. Aproveite o filme!")
else:
    print("Desculpe, não há mais poltronas disponíveis para o filme " + filmeEscolhido + ".")

print("")
print("================================")
snacks = ["Pipoca", "Refrigerante", "Chocolate", "Salgadinho", "Sorvete"]

print("Aqui estão os snacks disponíveis para acompanhar o filme:")
print(snacks)
print("Deseja comprar algum Snack para acompanhar o filme? (sim/não)")
respostaSnack = input("sim/não: ")
if(respostaSnack == "sim"):
    print("Qual snack você gostaria de comprar?")
    snackEscolhido = input("Qual snack você gostaria de comprar? ")
    if(snackEscolhido in snacks):
        print("Snack " + snackEscolhido + " comprado. Aproveite o filme!")
    else:
        print("Desculpe, o snack " + snackEscolhido + " não está disponível.")
else:
    print("Tudo bem, aproveite o filme sem snacks!")


print("")
print("================================")
print("")
print("Obrigado por escolher o CinePython, " + name + "! Aproveite o filme e volte sempre!")
print("")
print("================================")
print("")
print("Filme: " + filmeEscolhido)
print("Poltrona: " + poltronaEscolhida)
if(respostaSnack == "sim"):
    print("Snack: " + snackEscolhido)
else:
    print("Snack: Nenhum")
print("================================")
print("")
