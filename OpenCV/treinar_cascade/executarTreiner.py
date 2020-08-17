import os

if not os.path.exists('infos'):
    os.makedirs('infos')

if not os.path.exists('vetores'):
    os.makedirs('vetores')
    
if not os.path.exists('data'):
    os.makedirs('data')

if not os.path.exists('negativas'):
    os.makedirs('negativas')

if not os.path.exists('positivas'):
    os.makedirs('positivas')

if not os.path.exists('feias'):
    os.makedirs('feias')

if not os.listdir('negativas'):
    os.system("python3 download.py")
    os.system("python3 imgFeias.py")
    os.system("python3 renomear.py")
    

if not os.path.exists('bg.txt'):
    os.system("python3 listar.py")

os.system("sudo apt install libopencv-dev")

cont = 1
positivas = 0

num = 0
for x in os.listdir('negativas'):
    num += 1

#criar varias amostras com as imagens positivas
for img in os.listdir('positivas'):
    imgDir = 'positivas/'+img
    infosDir = 'infos/info{0}/info.lst'.format(cont)
    comando = ('opencv_createsamples -img {0} -bg bg.txt -info {1} -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num {2}'.format(imgDir, infosDir, num))
    os.system(comando)
    cont +=1

positivas = cont
numPos = (num * positivas) - (500 * positivas)
if (numPos % 2 != 0):
    numPos = numPos - 1
numNeg = numPos/2

cont = 1

#criar os arquivos de vetores
for vect in os.listdir('infos'):
    vecDir = 'infos/{0}/info.lst'.format(vect)
    infosDir = 'vetores/positives{0}.vec'.format(cont)
    comando = ('opencv_createsamples -info {0} -num {1} -w 20 -h 20 -vec {2}'.format(vecDir, num, infosDir))
    os.system(comando)
    cont += 1

os.system('python3  mergevec.py -v vetores -o positives.vec')

for x in range(10):
    print(".")

numEst = 10
print('////////////////////////////////')
print('numPos: ',int(numPos))
print('numNeg: ',int(numNeg))
print('////////////////////////////////')
opc = input('alterar valor de numPos e numNeg (N => não; S => sim)')
if (opc == 'S' or opc == 'S') :
    numEst = int(input('Estagios(min 10): '))
    numPos = int(input('numPos: '))
    numNeg = int(input('numNeg: '))

comando = 'opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos {0} -numNeg {1} -numStages {2} -w 20 -h 20'.format(numPos, numNeg, numEst)
os.system(comando)

print("FINALIZADO !!!")