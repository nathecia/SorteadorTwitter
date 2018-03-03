import participantes
import random 

lista = participantes.get()
sorteados = []

def sortear ():
  while not len(lista) == len(sorteados):
    selecionado = random.randrange (0,len(lista),1)

    if not selecionado in sorteados:
      return selecionado

  return None

while True:
  print "Numero total de twites: {}".format(len(lista) - len(sorteados))
  l = raw_input("Sortear: s\nSair: q\n>> ")
  if (l == "q"):
    break
  selecionado = sortear()
  
  if not selecionado == None:
    sorteados.append(selecionado)

    print "\n>>>>>>>>>>>"
    print lista[selecionado]
    print "<<<<<<<<<<<\n"
  else:
    print "Todos os participantes foram selecionados!"
    break
