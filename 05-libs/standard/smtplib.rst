smtplib — cliente de protocolo SMTP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El módulo ``smtplib`` define un cliente del protocolo :term:SMTP
(*Simple Mail TRansfer Protocol*), que puede ser usado para enviar
correo  electrónico a cualquier ordenador en Internet que esté
ejecutando un demonio SMTP o ESMTP.

El siguiente ejemplo compone un mensaje, ayudándose de la clase
``Message`` definido en ``email.message``. Las variables
``gmail_user`` y ``gmail_password`` están definidas en el código, lo
que quizá no sea la mejor de las ideas posibles. Una vez creado el
mensaje, se realiza la conexión al servidor de correo, que en este
caso es el de Google Mail. La conexión en este caso es un poco más
complicada de lo que sería con un servidor SMTP local, en la que la
seguridad a lo mejor es un poco más laxa:


    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    from email.message import Message
    from smtplib import SMTP

    gmail_user = 'tuusuario@gmail.com'
    gmail_password = 'tu contraseña'

    # Creamos el mensaje
    msg = Message()
    msg['to'] = 'euribates+test@gmail.com'
    msg['from'] = 'euribates@gmail.com'
    msg['subject'] = 'Esto es una prueba!'
    msg.set_payload('Hola, mundo\n\n-- Juan')

    # Lo enviamos
    print('Enviando correo', end=' ')
    smtpserver = SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_password)
    smtpserver.sendmail(gmail_user, msg['to'], msg.as_string())
    smtpserver.close()
    print('[OK]')


Aunque el formato de los mensajes es realmente sencillo, usar la clase
``Message`` nos permite incluir de forma rápida y sencilla
funcionalidades más elaboradas, como anexar ficheros o enviar
múltiples versiones del mismo contenido.

