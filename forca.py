import random

def carregar_palavras():
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        palavras = arquivo.readlines()
    return [palavra.strip().lower() for palavra in palavras]

def escolher_palavra(palavras):
    return random.choice(palavras)

def jogar_forca(palavra):
    palavra_escondida = ["_" if letra.isalpha() else letra for letra in palavra]
    letras_erradas = []
    tentativas = 6

    while tentativas > 0:
        letra_usuario = input("\nType a letter: ").lower()

        if letra_usuario.isalpha() and len(letra_usuario) == 1:
            if letra_usuario in palavra:
                for i in range(len(palavra)):
                    if palavra[i] == letra_usuario:
                        palavra_escondida[i] = letra_usuario
            else:
                letras_erradas.append(letra_usuario)
                tentativas -= 1

            print("Word: ", " ".join(palavra_escondida))
            print("Wrong letters: ", " ".join(letras_erradas))
            print(f"Remaining attempts: {tentativas}")

            if "_" not in palavra_escondida:
                print("\nCONGRATULATIONS! YOU WIN!")
                break
        else:
            print("Please enter a valid letter.")

    if tentativas == 0:
        print("\nGame over! The word was:", palavra)

if __name__ == "__main__":
    print("Welcome to the HANGMAN GAME!")

    palavras = carregar_palavras()
    palavra_secreta = escolher_palavra(palavras)

    print("Tip: The word has", len(palavra_secreta), "letters.")
    
    jogar_forca(palavra_secreta)