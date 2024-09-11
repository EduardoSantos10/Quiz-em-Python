print("Você Inicou o Quiz do Eduardo, Bem Vindo Irmãos(as)!")
user = input("Vamos Começar? (y/n) ")
# Variaver 'user' está recebendo a resposta da pergunta, já que o input
# Tem a função de pegar resposta do usuário/cliente.

print(user)
#Digitando sua respota, ela será armazenada.

if user != "y":

    quit()

# Sistema de Pontos
score = 0

print("Iniciando...")
# Através da cond. IF irei verificar se a resposta é verdadeira ou falsa.
# Se o user for diferente de "y" o prog. irá encerrar.
# Função "Quit" irá encerrar o códifo se a resposta for diferente.

print("Qual a capital da (Letônia)?\n (A)Riga \n (B)Berlim \n (C)Santiago \n")

questaoUm = input("Resposta: ")

if questaoUm == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

# A variável score será validada cada vez que meu usuário acertar uma respota,
# Irei atribuir o valor atual +1 como cada pergunta certa.

#Condição vai avaliar se a sua resposta está correta ou não, sendo correta, você prossiga.

print("Qual a capital da (Ucrania)?\n (A)Moscou \n (B)Kiev \n (C)Atenas \n")

questaoDois = input("Resposta: ")

if questaoUm == "B":
    print("Correto!")
else:
    print("Incorreto!")



print("Qual a capital da (Equador)?\n (A)Buenos Aires \n (B)Quito \n (C)Guayaquil \n")

questaoUm = input("Resposta: ")

if questaoUm == "B":
    print("Correto!")
else:
    print("Incorreto!")