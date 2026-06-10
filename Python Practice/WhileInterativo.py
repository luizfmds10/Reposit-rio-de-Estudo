nome = "Jailton Lemos"
numnomes = len(nome)

indice = 0
novoNome = ''

while numnomes > indice:
    letra = nome[indice]
    novoNome += letra
    novoNome += "*"
    indice += 1

print(novoNome)

