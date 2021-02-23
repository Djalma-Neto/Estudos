import os

if not os.path.exists('folder'):
    os.makedirs('folder')

paths = os.listdir('./folder')
NewText = open('./folder/NewText.txt', 'w+')

for x in paths:
    arquivo = open("./folder/{0}".format(x), "r")
    for linha in arquivo.readlines():
        if (linha):
            if('email' in linha or 'password' in linha):
                linha = linha.replace('email=', '')
                if ('password' in linha): linha = linha+'\n'
                linha = linha.replace('password=', '')
                NewText.write(linha)
