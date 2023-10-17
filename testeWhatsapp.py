import json

from WPP_Whatsapp import Create

# start client with your session name
your_session_name = "test"
creator = Create(session=your_session_name)
client = creator.start()
# Now scan Whatsapp Qrcode in browser

# check state of login
while creator.state != 'CONNECTED':
    raise Exception(creator.state)



# Simple message
result = client.getAllContacts()

cont = 1
for contato in result:
    if (contato["formattedName"] != None and contato["pushname"] != None and client.getContact(contato["id"]["_serialized"])["isMyContact"]):
       # print(f'{contato["pushname"]}  ***   {contato["shortName"]}   ***  {contato["id"]}')
       # print(client.getContact(contato["id"]["_serialized"])["formattedName"])

       print(f'{cont} - o número {contato["id"]["_serialized"].replace("@c.us", "")} é do contato  {client.getContact(contato["id"]["_serialized"])["formattedName"]}')
       cont += 1





creator