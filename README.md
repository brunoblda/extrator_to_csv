# 1. Extrator to csv

Transforma os arquivos gerados no extrator (.REF e .TXT) em arquivo .csv com o cabeçalho embutido.

Também realiza a inclusão das colunas de orgao e matricula de acordo com a coluna GR-MATRICULA

## 1.1 Forma de utilização

Salvar o arquivo executavel na pasta que contem os 2 arquivos e clicar 2 vezes no arquivo para executa-lo.

O programa é capaz de gerar os arquivos csv de independente da quantidade de duplas de arquivos que se encontram na pasta.

O arquivo somente transforma a dupla de arquivos em um arquivo csv caso não haja outro arquivo csv na pasta, assim, caso queria gerar um novo arquivo csv deve se tirar o ultimo arquivo csv gerado da dupla de arquivos da pasta.

## 1.2 Requerimentos 

Os modulos utilizados se encontram no arquivo requirements.txt.

Foi utilizado o python 3.10.8.

## 1.3 Executável

Para gerar o executável foi utilizado o modulo pyinstaller versão 5.0.

Foi executado o commando no powershell como administrador:

``` Bash
pyinstaller --onefile --paths .\venv\Lib\site-packages main.py
```