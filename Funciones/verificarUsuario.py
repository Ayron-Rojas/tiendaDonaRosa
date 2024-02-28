import telebot

usuarios = {
    "Rosita": "1234", # Reemplazar por los que la señora quiera
    "Airon": "5678" # Dejar de respaldo
}

def autentificarUsuario(bot, mensaje):
    palabras = mensaje.text.split()[1:]
    
    if len(palabras) != 2:
        bot.reply_to(mensaje, "Por favor, proporciona un usuario y contraseña.")
        return    
    
    usuario = palabras[0]
    contraseña = palabras[1]
    
    if usuario in usuarios and usuarios[usuario] == contraseña:
        bot.reply_to(mensaje, "Te has logeado correctamente.")
        return True
    else:
        bot.reply_to(mensaje, "Por favor, proporciona un usuario y contraseña correctos.")
        return False    
    
     