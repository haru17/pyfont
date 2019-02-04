# Pyfont 0.1
Script feito em Python3 para baixar e instalar fontes do site [dafont.com](https://www.dafont.com/) nos sistemas Linux.

## Instalação
Para instalar, basta clonar ou baixar este repositório. E em seguida executar o arquivo pyfont.py
ou mudar as permissões para executá-lo como script:

```
chmod +x pyfont.py
```

## Uso
Para utilizar o script você deve visitar o site [dafont.com](https://www.dafont.com/), escolher sua fonte e
copiar o link do botão de download, conforme a imagem abaixo:

![Print](https://i.imgur.com/RB1tehR.png)

E no terminal executar o script, colando o link copiado:

```
python3 pyfont.py https://dl.dafont.com/dl/?f=north_roksy
```
Ou caso modifique as permissões do script:

```
./pyfont https://dl.dafont.com/dl/?f=north_roksy
```

Obs: Caso seu terminal possua suporte para arraste, 
você só precisa arrastar o botão de download para ele.
