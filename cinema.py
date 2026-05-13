print("     ================================")
print("        Bem Vindo ao CinePython!!!   ")
print("     ================================")

filmes18 = ["O Poderoso Chefão", "Pulp Fiction", "O Senhor dos Anéis", "Matrix", "Clube da Luta"]
idadeMinima18 = 18
filmesMenores = ["Toy Story", "Frozen", "Procurando Nemo", "Shrek", "Meu Malvado Favorito"]
idadeMinimaMenores = 0

print("")
name = input("Escreva seu Nome: ")
print("Aoba, " + name + "!")
idade = input("Insira sua idade: ")
print("Você tem " + idade + " anos!")
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
    if(int(idade) >= idadeMinima18):
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

if(poltronas > 0):
    print("Há ", poltronas, " poltronas disponíveis para o filme " + filmeEscolhido + ".")
    poltronaEscolhida = input("Escolha uma poltrona (a1-a10 - g1-g10): ")
    poltronasJaEscolhidas.append(poltronaEscolhida)
    poltronas -= 1
    print("Poltrona " + poltronaEscolhida + " escolhida. Aproveite o filme!")
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
