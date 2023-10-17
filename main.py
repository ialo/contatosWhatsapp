
import time

from WPP_Whatsapp import Create

# start client with your session name
your_session_name = "test"
creator = Create(session=your_session_name, waitForLogin=True)

client = creator.start()

print(f'Conectado {client}')

time.sleep(5)

# Now scan Whatsapp Qrcode in browser

# check state of login
while creator.state != 'CONNECTED':
    raise Exception(creator.state)



# Simple message
result = client.getAllContacts()


resultado = []
cont = 0
for contato in result:
    if (contato["formattedName"] != None and contato["pushname"] != None and client.getContact(contato["id"]["_serialized"])["isMyContact"]):
       # print(f'{contato["pushname"]}  ***   {contato["shortName"]}   ***  {contato["id"]}')
       # print(client.getContact(contato["id"]["_serialized"])["formattedName"])

       numero = contato["id"]["_serialized"].replace("@c.us", "")
       nome = client.getContact(contato["id"]["_serialized"])["formattedName"]
       cont += 1

       dictemp = {'ordem': cont, 'numero': numero, 'nome': nome}

       resultado.append(dictemp)

       # print(f'{cont} - o número {contato["id"]["_serialized"].replace("@c.us", "")} é do contato  {client.getContact(contato["id"]["_serialized"])["formattedName"]}')

print(type(resultado))
for contato in resultado:
    print(f" ordem - {contato['ordem']}    nome = {contato['nome']}     numero = {contato['numero']}")



