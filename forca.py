import random

def escolher_palavra():
    palavras = ["python", "computador", "programacao", "terminal", "linux", "openai"]
    return random.choice(palavras)

def jogo_forca():
    palavra = escolher_palavra()
    letras_descobertas = ["_" for _ in palavra]
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra.")

    while tentativas > 0 and "_" in letras_descobertas:
        print("\nPalavra:", " ".join(letras_descobertas))
        print(f"Tentativas restantes: {tentativas}")
        print("Letras erradas:", " ".join(letras_erradas))

        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Digite apenas uma letra.")
            continue

        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
            print(f"Boa! A letra '{letra}' está na palavra.")
        else:
            tentativas -= 1
            letras_erradas.append(letra)
            print(f"A letra '{letra}' não está na palavra.")

    if "_" not in letras_descobertas:
        print("\nParabéns! Você adivinhou a palavra:", palavra)
    else:
        print("\nVocê perdeu! A palavra era:", palavra)

# Loop principal para jogar novamente ou sair
while True:
    jogo_forca()
    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar! Até a próxima!")
        break
