import numpy as np
from typing import Tuple

def gerar_matrizes_de_permutacao(N : int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gera duas matrizes de permutação de tamanho N x N.
    """

    I = np.eye(N)
    P = np.random.permutation(I)
    Q = np.random.permutation(I)

    return P, Q


def criar_alfabeto():
    alfabeto = {}
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    
    for i, letra in enumerate(letras):
        vetor = np.zeros(len(letras))
        vetor[i] = 1
        alfabeto[letra] = vetor
    
    return alfabeto

def encriptar_enigma(mensagem : str,
              P : np.ndarray,
              Q : np.ndarray) -> str:
    
    # dicionario para mapear as letras do alfatedo
    alfabeto = criar_alfabeto()

    encrypted_message = ""
    for letra in mensagem:
        if letra in alfabeto:
            # Multiplica o vetor da letra por P, depois por Q
            letra_codificada = Q @ (P @ alfabeto[letra])
            # Acha a letra correspondente no dicionario inverso
            for key, value in alfabeto.items():
                if np.allclose(value, letra_codificada):
                    encrypted_message += key
                    break
        else:
            encrypted_message += letra

    return encrypted_message
        


def decriptar_enigma(mensagem_encriptada : str,
              P : np.ndarray,
              Q : np.ndarray) -> str:
    alfabeto = criar_alfabeto()

    decrypted_message = ""
    for letra in mensagem_encriptada:
        if letra in alfabeto:
            # Multiplica o vetor da letra por Q^(-1), depois por P^(-1)
            letra_decodificada = np.linalg.inv(P) @ (np.linalg.inv(Q) @ alfabeto[letra])
            # Acha a letra correspondente no dicionário inverso
            for key, value in alfabeto.items():
                if np.array_equal(value, np.round(letra_decodificada).astype(int)):
                    decrypted_message += key
                    break
        else:
            decrypted_message += letra # Se não estiver no alfabeto, mantém o caractere original

    return decrypted_message

tamanho_alfabeto = len(criar_alfabeto())

mensagem = input("Digite uma mensagem: \n")

P, Q = gerar_matrizes_de_permutacao(tamanho_alfabeto)
mensagem_encriptada = encriptar_enigma(mensagem, P, Q)
mensagem_decriptada = decriptar_enigma(mensagem_encriptada, P, Q)

print('Mensagem original:', mensagem)
print('Mensagem encriptada:', mensagem_encriptada)
print('Mensagem decriptada:', mensagem_decriptada)