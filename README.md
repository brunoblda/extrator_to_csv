# Extrator to csv
Transforma os arquivos gerados no extrator (.REF e .TXT) em arquivo .csv com o cabeçalho embutido.
## Forma de utilização
Salvar o arquivo executavel na pasta que contem os 2 arquivos e clicar 2 vezes no arquivo para executa-lo.

O programa é capaz de gerar os arquivos csv de independente da quantidade de duplas de arquivos que se encontram na pasta.

O arquivo somente transforma a dupla de arquivos em um arquivo csv caso não haja outro arquivo csv na pasta, assim, caso queria gerar um novo arquivo csv deve se tirar o ultimo arquivo csv gerado da dupla de arquivos da pasta.
## Requerimentos 
Os modulos utilizados se encontram no arquivo requerements.txt.
Foi utilizado o python 3.10.8.
## Executável
Para gerar o executável foi utilizado o modulo pyinstaller versão 5.0.

Foi executado o commando:
``` Bash
pyinstaller --onefile --paths .\venv\Lib\site-packages main.py
```