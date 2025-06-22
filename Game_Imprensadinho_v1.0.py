from random import randint

def jogar():

    num_jogador = int(0)
    menor_numero = 0
    maior_numero = 51
    num_randomico = int(randint(2, 49))  # Gera um número aleatório entre 1 e 50)

    # print(num_randomico)  # Para testes, exibe o número secreto gerado aleatoriamente


    print("*********************************** \n| BEM VINDO AO JOGO IMPRENSADINHO |\n*********************************** \nO sistema irá sortear um número de forma randômica a cada partida. Seu objetivo é escolher o número antecessor e o sucessor do número secreto. \nCaso consiga imprensar o número secreto, você vence. \nSe acertar o número secreto, você perde.\nBoa sorte e bom jogo! \n")


    while True:
        # Mostra o intervalo de números válidos
        #if menor_numero is not None and maior_numero is not None:
        #    print("Digite um número entre 1 e 50.")

        try:
            num_jogador = int(input(f"Digite um número entre {menor_numero + 1} e {maior_numero - 1}: "))
        except ValueError:
            print(f"Digite um número inteiro válido. O número deve estar entre {menor_numero + 1} e {maior_numero - 1}: ")
            continue

        #Game Over
        if num_jogador == num_randomico:
            print("Game Over! Você acertou o número! \n O número secreto era: ", num_randomico)
            break

        # Atualiza o menor e maior número com base na jogada do jogador
        if (num_jogador > menor_numero + 1) and (num_jogador < num_randomico):
            menor_numero = num_jogador
            print("\n")
            
        if (num_jogador < maior_numero - 1) and (num_jogador > num_randomico):
            maior_numero = num_jogador
            print("\n")

        # Verifica se o jogador imprensou o número secreto
        if (menor_numero == (num_randomico - 1)) and (maior_numero == (num_randomico + 1)):
            print(f"********************************* \n            Parabéns! \n********************************* \nVocê imprensou o número secreto! \nVocê escolheu {menor_numero} e {maior_numero} \nO número secreto era: {num_randomico}")
            print("\nFim do jogo! \n")
            break     
while True:
    jogar()  # Executa o jogo

    resposta = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
    if resposta != 's':
        print("Obrigado por jogar! \nAté a próxima!")
        break