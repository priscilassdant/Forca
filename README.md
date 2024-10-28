# Forca
Jogo da forca em python para Linux e Termux.


# Jogo da Forca

O **Jogo da Forca** é um jogo clássico onde o jogador deve adivinhar uma palavra letra por letra. 
O jogador tem um número limitado de tentativas antes de perder o jogo.

## Como Jogar

1. O jogo escolherá uma palavra aleatória.
2. Você deve adivinhar as letras da palavra.
3. Você tem 6 tentativas para adivinhar a palavra correta.

Código e instrução:

> Instale o Termux no seu celular;
> Abra um terminal (abre automaticamente assim que você entrar no app);
> Atualize a versão do termux, através do terminal, com o código a seguir (copiar o código, colar e dar enter):

pkg update && pkg upgrade

> Instale o python com os seguintes códigos (copiar o código, colar e dar enter):

pkg install python

> Verificar a versão do python (para confirmar se o mesmo foi instalado):

python --version

> Instale o git com os códigos a seguir (copiar o código, colar e dar enter):

pkg install git

> Verificar a versão do git (para confirmar se o mesmo foi instalado):

git --version

> Agora, cole o código disponível na sessão de "Instalação" e Jogue o Jogo Da Forca.

## Instalação

Clone o repositório (código abaixo) e execute o jogo:

```bash
git clone https://github.com/priscilassdant/Forca.git
cd Forca
python3 forca.py
