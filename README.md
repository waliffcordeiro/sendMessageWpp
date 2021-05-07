# Envio automático de mensagems via WhatsApp

## Requirements
- Python 3
- pip3

Tendo instalado os itens acima em seu ambiente, execute:
```
pip3 install -r requirements.txt
```

____
## Como utilizar

### Lista de Receptores
Escreva um nome de contato ou grupo por linha no arquivo **receptores.txt**

Obs: É importante que os nomes estejam escritos de maneira idêntica aos nomes dos contatos ou grupos que receberão a mensagem, caso contrário, outra pessoa ou grupo pode receber sua mensagem por engano.
____

### Mensagem
Escreva a mensagem que será enviada no arquivo **mensagem.txt**
____

### Executando o envio
No diretório do projeto, digite 
```
python3 whatsappbot.py
```
____