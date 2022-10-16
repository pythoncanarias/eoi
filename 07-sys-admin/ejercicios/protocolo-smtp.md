# Ejercicio protocolo smtp con smtplib

Puedes encontrar toda la documentación de la librería `smtplib` en la web oficial de Python:
[https://docs.python.org/3/library/smtplib.html](https://docs.python.org/3/library/smtplib.html)

## Mi primer email con smtplib

1. Arranca un servidor smtp en local con el siguiente comando:
```
python -m smtpd -c DebuggingServer -n localhost:1025
```

2. Importa la librería smptlib 


```python
import smtplib
```

3. Define las variables `smtp_server` y `port`.  
  - `smtp_server` debe contener un string con el nombre del servidor (mira el comando con el que has arrancado el servidor en el paso 1)
  - `port` debe contener un número entero con el puerto donde se ha arrancado el servidor (paso 1 también)


```python
smtp_server  = 'localhost'
port = 1025
```

4. Define las siguientes variables:
  - `sender_email`: dirección del remitente (puedes inventartela) - tipo string
  - `receiver_email`: direccion del destinatario (puedes inventartela también) - tipo string
  - `message`: contenido del mensaje - 
    - puedes incluir el Subject en el cuerpo del mensaje
    - si quieres enviar un mensaje de varias líneas, prueba a definir el mensaje entre tres comillas consecutivas
    - por ejemplo:  
      ```
      message = """
          Subject: Hi there
          This message is sent from Python."""
      ```


```python
sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
message = """
Subject: Hi there
This message is sent from Python."""
```

5. Envía el mensaje al servidor utilizando el siguiente código:


```python
with smtplib.SMTP(smtp_server, port) as server:
    server.sendmail(sender_email, receiver_email, message)
```

En la consola donde habías arrancado el servidor, deberías ver algo como esto:
```
---------- MESSAGE FOLLOWS ----------                                                                                b'X-Peer: 127.0.0.1'                                                                                                 b''                                                                                                                  b'Subject: Hi there'                                                                                                 b'This message is sent from Python.'                                                                                 ------------ END MESSAGE ------------  
```

6. Para entender bien qué pasos ha seguido el protocolo "por dentro", añade la siguiente línea al código justo antes de mandar el mensaje:
```
server.set_debuglevel(True)
```


```python
with smtplib.SMTP(smtp_server, port) as server:
    server.set_debuglevel(True)
    server.sendmail(sender_email, receiver_email, message)
```

    send: 'ehlo DESKTOP-89DFD33.localdomain\r\n'
    reply: b'250-DESKTOP-89DFD33.localdomain\r\n'
    reply: b'250-8BITMIME\r\n'
    reply: b'250 HELP\r\n'
    reply: retcode (250); Msg: b'DESKTOP-89DFD33.localdomain\n8BITMIME\nHELP'
    send: 'mail FROM:<my@gmail.com>\r\n'
    reply: b'250 OK\r\n'
    reply: retcode (250); Msg: b'OK'
    send: 'rcpt TO:<your@gmail.com>\r\n'
    reply: b'250 OK\r\n'
    reply: retcode (250); Msg: b'OK'
    send: 'data\r\n'
    reply: b'354 End data with <CR><LF>.<CR><LF>\r\n'
    reply: retcode (354); Msg: b'End data with <CR><LF>.<CR><LF>'
    data: (354, b'End data with <CR><LF>.<CR><LF>')
    send: b'\r\nSubject: Hi there\r\nThis message is sent from Python.\r\n.\r\n'
    reply: b'250 OK\r\n'
    reply: retcode (250); Msg: b'OK'
    data: (250, b'OK')
    send: 'QUIT\r\n'
    reply: b'221 Bye\r\n'
    reply: retcode (221); Msg: b'Bye'


Compara la salida de la consola con el ejemplo de una comunicación SMTP [según la wikipedia](https://es.wikipedia.org/wiki/Protocolo_para_transferencia_simple_de_correo): (seguro que el tuyo tiene algún `retcode` de más, pero deberías encontrar bastantes similitudes)

```
S: 220 Servidor SMTP
C: HELO miequipo.midominio.com
S: 250 Hello, please to meet you
C: MAIL FROM: <yo@midominio.com>
S: 250 Ok
C: RCPT TO: <destinatario@sudominio.com>
S: 250 Ok
C: DATA
S: 354 End data with <CR><LF>.<CR><LF>
C: Subject: Campo de asunto
C: From: yo@midominio.com
C: To: destinatario@sudominio.com
C:
C: Hola,
C: Esto es una prueba.
C: Hasta luego.
C:
C: .
C: <CR><LF>.<CR><LF>
S: 250 Ok: queued as 12345
C: quit
S: 221 Bye
```

## Extendiendo el servidor smtp

Como el servidor smtp por defecto no nos ofrece mucha información por defecto de la información que recibe, vamos a extender la funcionalidad de este servidor para que muestre por consola más datos.

Usaremos la herencia para crearnos una clase que herede del módulo `smtpd.SMTPServer` y reescribiremos su método `process_message` para imprimir toda la información que le llega (tienes toda la info sobre ese módulo y esa función [aquí](https://docs.python.org/3/library/smtpd.html?highlight=smtpd#smtpd.SMTPServer.process_message))

1. Para ello, crea un fichero llamado `email-server.py` e incluye el siguiente código en él:

```python
import smtpd
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, \
                        data, mail_options=None, rcpt_options=None):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to  :', rcpttos)
        print('Message length        :', len(data))


# Arranca el servidor en un proceso asíncrono
server = CustomSMTPServer(('127.0.0.1', 1025), None)
asyncore.loop()
```

2. Arranca el servidor usando este fichero con el siguiente comando:
```
python ejercicios/email-server.py
```

3. Reenvía el mensaje anterior al servidor:


```python
with smtplib.SMTP(smtp_server, port) as server:
    server.sendmail(sender_email, receiver_email, message)
```

Ahora verás más información en la consola, algo como esto:
    
```
Receiving message from: ('127.0.0.1', 50488)                                                                         Message addressed from: my@gmail.com                                                                                 Message addressed to  : ['your@gmail.com']                                                                           Message length        : 52 
```

## Usando la api de GMail

https://developers.google.com/gmail/api/quickstart/python/

1. Crear un fichero de credenciales siguiendo estas instrucciones: https://developers.google.com/workspace/guides/create-credentials

2. Instala las librerías de GMail


```python
!  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

    Collecting google-api-python-client
      Downloading google_api_python_client-2.3.0-py2.py3-none-any.whl (7.1 MB)
    [K     |████████████████████████████████| 7.1 MB 6.9 MB/s eta 0:00:01
    [?25hCollecting google-auth-httplib2
      Downloading google_auth_httplib2-0.1.0-py2.py3-none-any.whl (9.3 kB)
    Collecting google-auth-oauthlib
      Downloading google_auth_oauthlib-0.4.4-py2.py3-none-any.whl (18 kB)
    Collecting google-auth<2dev,>=1.16.0
      Downloading google_auth-1.30.0-py2.py3-none-any.whl (146 kB)
    [K     |████████████████████████████████| 146 kB 87.1 MB/s eta 0:00:01
    [?25hRequirement already satisfied: six<2dev,>=1.13.0 in /mnt/c/Users/alicia/workspace/eoi/eoi-administracion-sistemas/.venv/lib/python3.8/site-packages (from google-api-python-client) (1.15.0)
    Collecting uritemplate<4dev,>=3.0.0
      Downloading uritemplate-3.0.1-py2.py3-none-any.whl (15 kB)
    Collecting google-api-core<2dev,>=1.21.0
      Downloading google_api_core-1.26.3-py2.py3-none-any.whl (93 kB)
    [K     |████████████████████████████████| 93 kB 1.3 MB/s  eta 0:00:01
    [?25hCollecting httplib2<1dev,>=0.15.0
      Downloading httplib2-0.19.1-py3-none-any.whl (95 kB)
    [K     |████████████████████████████████| 95 kB 2.4 MB/s  eta 0:00:01
    [?25hCollecting googleapis-common-protos<2.0dev,>=1.6.0
      Downloading googleapis_common_protos-1.53.0-py2.py3-none-any.whl (198 kB)
    [K     |████████████████████████████████| 198 kB 91.1 MB/s eta 0:00:01
    [?25hCollecting protobuf>=3.12.0
      Downloading protobuf-3.16.0-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.0 MB)
    [K     |████████████████████████████████| 1.0 MB 84.7 MB/s eta 0:00:01
    [?25hRequirement already satisfied: packaging>=14.3 in /mnt/c/Users/alicia/workspace/eoi/eoi-administracion-sistemas/.venv/lib/python3.8/site-packages (from google-api-core<2dev,>=1.21.0->google-api-python-client) (20.9)
    Collecting requests<3.0.0dev,>=2.18.0
      Using cached requests-2.25.1-py2.py3-none-any.whl (61 kB)
    Requirement already satisfied: setuptools>=40.3.0 in /mnt/c/Users/alicia/workspace/eoi/eoi-administracion-sistemas/.venv/lib/python3.8/site-packages (from google-api-core<2dev,>=1.21.0->google-api-python-client) (44.0.0)
    Collecting pytz
      Downloading pytz-2021.1-py2.py3-none-any.whl (510 kB)
    [K     |████████████████████████████████| 510 kB 79.3 MB/s eta 0:00:01
    [?25hCollecting rsa<5,>=3.1.4
      Downloading rsa-4.7.2-py3-none-any.whl (34 kB)
    Collecting cachetools<5.0,>=2.0.0
      Downloading cachetools-4.2.2-py3-none-any.whl (11 kB)
    Collecting pyasn1-modules>=0.2.1
      Downloading pyasn1_modules-0.2.8-py2.py3-none-any.whl (155 kB)
    [K     |████████████████████████████████| 155 kB 91.0 MB/s eta 0:00:01
    [?25hRequirement already satisfied: pyparsing<3,>=2.4.2 in /mnt/c/Users/alicia/workspace/eoi/eoi-administracion-sistemas/.venv/lib/python3.8/site-packages (from httplib2<1dev,>=0.15.0->google-api-python-client) (2.4.7)
    Collecting pyasn1<0.5.0,>=0.4.6
      Downloading pyasn1-0.4.8-py2.py3-none-any.whl (77 kB)
    [K     |████████████████████████████████| 77 kB 5.4 MB/s  eta 0:00:01
    [?25hCollecting urllib3<1.27,>=1.21.1
      Using cached urllib3-1.26.4-py2.py3-none-any.whl (153 kB)
    Collecting chardet<5,>=3.0.2
      Using cached chardet-4.0.0-py2.py3-none-any.whl (178 kB)
    Collecting certifi>=2017.4.17
      Using cached certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
    Collecting idna<3,>=2.5
      Using cached idna-2.10-py2.py3-none-any.whl (58 kB)
    Collecting requests-oauthlib>=0.7.0
      Downloading requests_oauthlib-1.3.0-py2.py3-none-any.whl (23 kB)
    Collecting oauthlib>=3.0.0
      Downloading oauthlib-3.1.0-py2.py3-none-any.whl (147 kB)
    [K     |████████████████████████████████| 147 kB 93.5 MB/s eta 0:00:01
    [?25hInstalling collected packages: pyasn1, urllib3, rsa, pyasn1-modules, protobuf, idna, chardet, certifi, cachetools, requests, pytz, oauthlib, httplib2, googleapis-common-protos, google-auth, uritemplate, requests-oauthlib, google-auth-httplib2, google-api-core, google-auth-oauthlib, google-api-python-client
    Successfully installed cachetools-4.2.2 certifi-2020.12.5 chardet-4.0.0 google-api-core-1.26.3 google-api-python-client-2.3.0 google-auth-1.30.0 google-auth-httplib2-0.1.0 google-auth-oauthlib-0.4.4 googleapis-common-protos-1.53.0 httplib2-0.19.1 idna-2.10 oauthlib-3.1.0 protobuf-3.16.0 pyasn1-0.4.8 pyasn1-modules-0.2.8 pytz-2021.1 requests-2.25.1 requests-oauthlib-1.3.0 rsa-4.7.2 uritemplate-3.0.1 urllib3-1.26.4



```python
import os
import pickle

# Gmail API utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
```

3. Autentícate con este código


```python
from google.oauth2.credentials import Credentials

SCOPES = ['https://mail.google.com/']
token_file = '/mnt/c/Users/alicia/workspace/eoi-administracion-sistemas/.eoi_solutions/token.json'

def gmail_authenticate():
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(token_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)
```


```python
# get the Gmail API service
service = gmail_authenticate()
```

    Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=167484279656-b98n4ann0qjh8ad2haoph6hjqevvucgu.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A59113%2F&scope=https%3A%2F%2Fmail.google.com%2F&state=VLLTYHzh7O7czm8uqocOaK0z0LUHhs&access_type=offline


4. Prueba a mostrar las etiquetas de tu buzón de correo para comprobar que la conexión va bien


```python
results = service.users().labels().list(userId='me').execute()
labels = results.get('labels', [])

if not labels:
    print('No labels found.')
else:
    print('Labels:')
    for label in labels:
        print(label['name'])
```

    Labels:
    CHAT
    SENT
    INBOX
    IMPORTANT
    TRASH
    DRAFT
    SPAM
    CATEGORY_FORUMS
    CATEGORY_UPDATES
    CATEGORY_PERSONAL
    CATEGORY_PROMOTIONS
    CATEGORY_SOCIAL
    STARRED
    UNREAD
    Casa
    Ing Direct
    Mis Viajes/París
    Productos
    Estudios
    Casa/evo
    DjangoGirls Online 2020
    Linea Directa
    Kloshletter
    Eptisa
    Personal
    Mis Viajes/Polonia
    Mis Viajes/Suecia
    Casa/openbank
    Mis Viajes
    Amazon
    Alquiler Carlos Arniches
    Planes
    MBIT School
    Pisos
    StyleSage
    Inpro Medio Ambiente
    Alquiler Delicias 28
    Mis Viajes/Cuba
    Mis Viajes/Lanzarote
    Mis Viajes/Malasia & Singapur
    Mis Viajes/Japón
    Michos


5. Ahora crea dos funciones auxiliares para crear y enviar mensajes


```python
from email.mime.text import MIMEText
from base64 import urlsafe_b64decode, urlsafe_b64encode

def create_message(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}
```


```python
def send_message(service, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId='me', body=message)
               .execute())
    print(f'Message Id: {message["id"]}')
    return message
  except errors.HttpError as error:
    print(f'An error occurred: {error}')
```

6. Envía un mensaje usando las funciones que acabamos de crear


```python
message = create_message('apj.ali@gmail.com', 'apj.ali@gmail.com', 'Prueba curso EOI', 'Esta es una prueba')
send_message(service, message)
```

    Message Id: 1794e6b1fdf1be2c





    {'id': '1794e6b1fdf1be2c',
     'threadId': '1794e6b1fdf1be2c',
     'labelIds': ['UNREAD', 'SENT', 'INBOX']}


