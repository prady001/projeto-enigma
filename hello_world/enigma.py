import numpy as np
from types import Tuple

def gerar_matrizes_de_permutacao(N : int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gera duas matrizes de permutação de tamanho N x N.
    """

    I = np.eye(N)
    P = np.random.permutation(I)
    Q = np.random.permutation(I)

    return P, Q

def encriptar_enigma(mensagem : str,
              P : np.ndarray,
              Q : np.ndarray) -> str:
    
    raise NotImplementedError

def decriptar_enigma(mensagem_encriptada : str,
              P : np.ndarray,
              Q : np.ndarray) -> str:
    raise NotImplementedError
