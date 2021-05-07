from utils import *

# Tempo para acessar o WhatsApp Web (em segundos)
TEMPO_INICIAL = 30

driver.get('https://web.whatsapp.com/')
sleep(TEMPO_INICIAL)

receptores = open('receptores.txt', 'r').read().split('\n')
print (receptores)

mensagem = open('mensagem.txt', 'r').read()

for receptor in receptores:
    buscar_contato(receptor)
    enviar_mensagem(mensagem)