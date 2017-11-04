import random 

usuarios = []

arq = open ('tweets.txt','r')
usuarios = arq.readlines()

selecionado = random.randrange (0,len(usuarios),1)

print usuarios[selecionado]

arq.close()
