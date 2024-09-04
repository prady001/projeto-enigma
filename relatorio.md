# Projeto Enigma

Este projeto é uma implementação simples de uma máquina de encriptação e decriptação inspirada na famosa máquina Enigma, utilizando permutações de matrizes em Python.

## Descrição

O projeto utiliza álgebra linear para encriptar e decriptar mensagens. A ideia principal é representar cada letra de uma mensagem como um vetor unitário, aplicar transformações lineares através de matrizes de permutação, e depois mapear o vetor resultante de volta para uma letra. O processo inverso decodifica a mensagem.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- **enigma.py**: Contém as funções principais para geração de matrizes de permutação, criação do alfabeto, encriptação e decriptação das mensagens.
- **__init__.py**: Faz a inicialização do pacote.
- **main.py**: Um exemplo de aplicação simples que utiliza o módulo `hello_world`.
- **mylib.py**: Um módulo de exemplo que imprime "Hello world!".
- **setup.py**: Script de configuração para empacotar e distribuir o projeto.

## Operações Matemáticas

### Matrizes de Permutação

Uma matriz de permutação é uma matriz quadrada binária, onde em cada linha e em cada coluna existe exatamente um elemento igual a 1, e os demais elementos são 0. Essas matrizes são usadas para reordenar os elementos de um vetor.

Dada uma matriz de permutação `P` e um vetor `v`, a multiplicação `P @ v` permuta os elementos de `v` de acordo com `P`.

### Encriptação e Decriptação

O processo de encriptação pode ser descrito como:
1. Representar cada letra da mensagem como um vetor unitário utilizando o alfabeto gerado.
2. Aplicar duas transformações lineares sucessivas à matriz de permutação `P` seguida por `Q`.
3. O vetor resultante é então mapeado de volta para a letra correspondente.

A decriptação é o processo inverso:
1. Multiplicar o vetor codificado pelas inversas de `Q` e `P` na ordem inversa (`Q⁻¹ @ P⁻¹`).
2. Mapear o vetor resultante de volta para a letra correspondente.

## Montagem do Alfabeto

### Como o Alfabeto é Criado

A função `criar_alfabeto()` constrói um dicionário que mapeia cada caractere (letra maiúscula, letra minúscula e o espaço) para um vetor unitário correspondente. 

#### Passo a Passo:

1. **Definição das Letras**:
    - A função começa definindo uma string que contém todos os caracteres que serão utilizados: `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ` (todas as letras do alfabeto em maiúsculas e minúsculas, além do espaço).

2. **Inicialização do Dicionário**:
    - Um dicionário chamado `alfabeto` é criado, onde cada chave será uma letra (ou o espaço) e o valor associado será um vetor unitário (um vetor com um único valor 1 e os demais valores 0).

3. **Criação dos Vetores Unitários**:
    - A função itera sobre cada letra na string de letras. Para cada letra, um vetor de zeros com comprimento igual ao número total de letras (62, no caso) é criado.
    - O vetor é então preenchido com o valor 1 na posição correspondente à ordem da letra na string. Por exemplo, a letra 'A' será mapeada para o vetor `[1, 0, 0, ..., 0]`, a letra 'B' para `[0, 1, 0, ..., 0]` e assim por diante.

4. **Mapeamento no Dicionário**:
    - Cada vetor unitário é então associado à sua respectiva letra no dicionário `alfabeto`.

### Exemplo:

Se o alfabeto for composto por 3 letras: `A`, `B` e `C`, a função `criar_alfabeto()` produziria o seguinte dicionário:

alfabeto = {
    'A': [1, 0, 0],
    'B': [0, 1, 0],
    'C': [0, 0, 1],
    ' ': [0, 0, 0]  # O espaço é um vetor de zeros
}

Este mapeamento permite que cada letra seja representada como um vetor que pode ser transformado por meio de operações matriciais.

### Importância no Processo de Encriptação

Este dicionário é essencial para o processo de encriptação e decriptação, pois permite que cada caractere da mensagem seja transformado em um vetor que pode ser manipulado pelas matrizes de permutação. Após a manipulação, o vetor transformado é convertido de volta em uma letra usando este mesmo dicionário.

## Como Funciona

### Funções Principais

#### `gerar_matrizes_de_permutacao(N: int) -> Tuple[np.ndarray, np.ndarray]`

Esta função gera duas matrizes de permutação `P` e `Q` de tamanho `N x N`. Cada uma é uma matriz de identidade reordenada aleatoriamente.

- **Parâmetros**:
  - `N`: Tamanho das matrizes (correspondente ao número de letras do alfabeto).

- **Retorno**:
  - `P`: Primeira matriz de permutação.
  - `Q`: Segunda matriz de permutação.

#### `criar_alfabeto() -> dict`

Cria um dicionário que mapeia cada letra do alfabeto (maiúsculas, minúsculas e espaço) para um vetor unitário.

- **Retorno**:
  - `alfabeto`: Um dicionário onde as chaves são as letras e os valores são vetores unitários.

#### `encriptar_enigma(mensagem: str, P: np.ndarray, Q: np.ndarray) -> str`

Encripta uma mensagem utilizando as matrizes de permutação `P` e `Q`.

- **Operação**:
  - Para cada letra na mensagem, o vetor correspondente é multiplicado por `P` e depois por `Q`.
  - O vetor resultante é convertido de volta para a letra correspondente.

- **Parâmetros**:
  - `mensagem`: A mensagem que será encriptada.
  - `P`: A primeira matriz de permutação.
  - `Q`: A segunda matriz de permutação.

- **Retorno**:
  - `encrypted_message`: A mensagem encriptada.

#### `decriptar_enigma(mensagem_encriptada: str, P: np.ndarray, Q: np.ndarray) -> str`

Decripta uma mensagem utilizando as inversas das matrizes de permutação `P` e `Q`.

- **Operação**:
  - Para cada letra na mensagem encriptada, o vetor correspondente é multiplicado pela inversa de `Q` e depois pela inversa de `P`.
  - O vetor resultante é convertido de volta para a letra correspondente.

- **Parâmetros**:
  - `mensagem_encriptada`: A mensagem que será decriptada.
  - `P`: A primeira matriz de permutação usada na encriptação.
  - `Q`: A segunda matriz de permutação usada na encriptação.

- **Retorno**:
  - `decrypted_message`: A mensagem decriptada.

### Exemplo de Uso

```python
$ python enigma.py
Digite uma mensagem: 
Hello World
Mensagem original: Hello World
Mensagem encriptada: fGhkl iOpqr
Mensagem decriptada: Hello World
```

## Instalação

Para instalar o projeto, execute o seguinte comando:

```bash
pip install git+https://github.com/usuario/repositorio.git
```

A segunda maneira é clonar o repositório e fazer uma instalação local:

```bash
git clone https://github.com/prady001/projeto-enigma.git
cd projeto-enigma
pip install .
```

Após instalar, o programa `tiago_hello_world` deve estar instalado. Então, executando o comando:

```bash
cd hello_world
python enigma.py
```

seu programa deveria imprimir a string `Digite uma mensagem:` na tela

## Como Executar

Você pode executar o script `enigma.py` diretamente:

```bash
python enigma.py
```

## Dependências

- Python 3.11 ou superior
- NumPy

As dependências necessárias estão listadas no arquivo `requirements.txt`.

## Estrutura de Pastas

```
hello_world/
├── assets/
│       ├── poetry.txt
│       └── test_folder/
│       └── test_something.txt
├── __init__.py
├── enigma.py
├── main.py
├── mylib.py
├── README.md
├── requirements.txt
└── setup.py
```

## Autores

- Gabriel Alencar e Manuela Saragoça
