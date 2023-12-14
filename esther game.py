#friends game

import time

personagens = {
"Ross": 0,
"Chandler" : 0,
"Joey": 0,
"Monica": 0,
"Rachel": 0,
"Phoebe": 0
}


time.sleep (2)
user_name = input ("Qual seu nome? ")
time.sleep(1)
print (f"\nBem vindo(a) {user_name} ")
time.sleep(1)
print ("Este é o teste de personalidade da série 'Friends' ")
print ("Vamos começar fazendo algumas perguntas para identificar qual personagem você mais se parece \n")
print ("Responda com as palavras em LETRAS MAIUSCULAS ")
time.sleep(1)
print("\n Carregando...\n")
time.sleep(2)

pergunta_1 = input ("Você é uma pessoa ENGRAÇADA ou SÉRIA? ")
while pergunta_1.lower() not in  ['engraçada' , 'séria']:
    print("Por favor, digite uma resposta válida")
    pergunta_1 = input ("\nVocê é uma pessoa ENGRAÇADA ou SÉRIA? ")

if pergunta_1.lower() == 'engraçada':
    personagens["Chandler"] += 1
    personagens["Joey"] += 1
    personagens["Phoebe"] += 1
    personagens["Ross"] += 1
elif pergunta_1.lower() == 'séria':
    personagens["Monica"] += 1
    personagens["Rachel"] += 1

time.sleep(3)
pergunta_2 = input ("\nVocê é uma pessoa ESPERTA ou DESLIGADA? ")
while pergunta_2.lower() not in  ['esperta' , 'desligada']:
    print("Por favor, digite uma resposta válida")
    pergunta_2 = input ("\nVocê é uma pessoa ESPERTA ou desligada? ")

if pergunta_2.lower() == 'esperta':
    personagens["Chandler"] +=1
    personagens["Monica"]
    personagens["Ross"]
elif pergunta_2.lower() == 'desligada':
    personagens["Joey"] += 1
    personagens["Phoebe"] += 1

time.sleep(3)
pergunta_3 = input ("\nEm suas escolhas você é uma pessoa RACIONAL ou PASSIONAL? ")
while pergunta_3.lower() not in  ['racional' , 'passional']:
    print("Por favor, digite uma resposta válida")
    pergunta_3 = input ("\nEm suas escolhas você é uma pessoa RACIONAL ou PASSIONAL? ")

if pergunta_3.lower() == 'racional':
    personagens["Monica"] += 1
    personagens["Chandler"] += 1
elif pergunta_3.lower() == 'passional':
    personagens["Joey"] += 1

    personagens["Phoebe"] += 1
    personagens["Rachel"] += 1
    personagens["Ross"] += 1

time.sleep(3)
pergunta_4 = input ("\nVocê é uma pessoa competitiva? (Responda com SIM ou NÃO) ")
while pergunta_4.lower() not in ['sim', 'não']:
    print("Por favor, digite uma resposta válida")
    pergunta_4 = input ("\nVocê é uma pessoa competitiva? (Responda com SIM ou NÃO) ")

if pergunta_4.lower() == 'sim':
    personagens["Monica"] +=1
    personagens["Chandler"] +=1
elif pergunta_4.lower() == 'não':
    personagens["Joey"] += 1
    personagens["Phoebe"] += 1
    personagens["Rachel"] += 1
    personagens["Ross"] += 1

time.sleep(3)
pergunta_5 = input ("\nVocê é uma pessoa espiritual? (Responda com SIM ou NÃO) ")
while pergunta_5.lower() not in ['sim', 'não']:
    print("Por favor, digite uma resposta válida")
    pergunta_5 = input ("\nVocê é uma pessoa espiritual? (Responda com SIM ou NÃO) ")

if pergunta_5 == 'sim':
    personagens["Phoebe"] += 1
elif pergunta_5 == 'não':
    personagens["Chandler"] += 1
    personagens["Joey"] += 1
    personagens["Monica"] += 1
    personagens["Rachel"] += 1
    personagens["Ross"] += 1

time.sleep(3)
pergunta_6 = input ("\nVocê se considera uma pessoa inteligente? (Responda com SIM ou NÃO) ")
while pergunta_6.lower() not in ['sim', 'não']:
    print("Por favor, digite uma resposta válida")
    pergunta_6 = input ("\nVocê se considera uma pessoa inteligente? (Responda com SIM ou NÃO) ")

if pergunta_6 == 'sim':
    personagens["Chandler"] += 1
    personagens["Monica"] += 1
    personagens["Ross"] += 1
elif pergunta_6 == 'não':
    personagens["Joey"] += 1
    personagens["Phoebe"] += 1
    personagens["Rachel"] += 1

time.sleep(3)
pergunta_7 = input ("\nEm seus relacionamentos, você é CIUMENTO ou TRANQUILO? ")
while pergunta_7.lower() not in ['ciumento', 'tranquilo']:
    print("Por favor, digite uma resposta válida")
    pergunta_7 = input ("\nEm seus relacionamentos, você é CIUMENTO ou TRANQUILO? ")

if pergunta_7 == 'ciumento':
    personagens["Chandler"] += 1
    personagens["Ross"] += 1
elif pergunta_7 == 'tranquilo':
    personagens["Joey"] += 1
    personagens["Monica"] += 1
    personagens["Phoebe"] += 1
    personagens["Rachel"] += 1

time.sleep(3)
pergunta_8 = input ("\nVocê é uma pessoa INTROVERTIDA ou EXTROVERTIDA? ")
while pergunta_8.lower() not in ['introvertida', 'extrovertida']:
    print("Por favor, digite uma resposta válida")
    pergunta_8 = input ("\nVocê é uma pessoa INTROVERTIDA ou EXTROVERTIDA? ")

if pergunta_8 == 'introvertida':
    personagens["Monica"] += 1
    personagens["Ross"] += 1
elif pergunta_8 == 'extrovertida':
    personagens["Chandler"] += 1
    personagens["Joey"] += 1
    personagens["Phoebe"] += 1
    personagens["Rachel"] += 1

time.sleep(3)
pergunta_9 = input("\nVocê se considera uma pessoa ingênua? (Responda com SIM ou NÃO) ")
while pergunta_9.lower() not in ['sim', 'não']:
    print("Por favor, digite uma resposta válida")
    pergunta_9 = input("\nVocê se considera uma pessoa ingênua? (Responda com SIM ou NÃO) ")

if pergunta_9 == 'sim':
    personagens["Joey"] += 1
    personagens["Phoebe"] += 1
elif pergunta_9 == 'não':
    personagens["Chandler"] += 1
    personagens["Monica"] += 1
    personagens["Rachel"] += 1
    personagens["Ross"] += 1

time.sleep(3)
pergunta_10 = input ("\nNormalmente você é a pessoa que BAGUNÇA tudo ou que ARRUMA tudo? ")
while pergunta_10.lower() not in ['bagunça', 'arruma']:
    print("Por favor, digite uma resposta válida")
    pergunta_10 = input ("\nNormalmente você é a pessoa que BAGUNÇA tudo ou que ARRUMA tudo? ")

if pergunta_10 == 'bagunça':
    personagens["Joey"] += 1
    personagens["Rachel"] += 1
elif pergunta_10 == 'arruma':
    personagens["Monica"] += 1
    personagens["Ross"] += 1

time.sleep(3)
pergunta_11 = input ("\nVocê gosta de praticar esportes? (Responda com SIM ou NÃO) ")
while pergunta_11.lower() not in ['sim', 'não']:
    print("Por favor, digite uma resposta válida")
    pergunta_11 = input ("\nVocê gosta de praticar esportes? (Responda com SIM ou NÃO) ")

if pergunta_11 == 'sim':
    personagens["Chandler"] += 1
    personagens["Joey"] += 1
    personagens["Monica"] += 1
    personagens["Ross"] +=1
elif pergunta_11 == 'não':
    personagens["Phoebe"] += 1
    personagens["Rachel"] += 1

time.sleep(3)


personagem_vencedor = max(personagens, key=personagens.get)
print(f"\n{user_name} seu personagem em Friends é: {personagem_vencedor}! \n")
