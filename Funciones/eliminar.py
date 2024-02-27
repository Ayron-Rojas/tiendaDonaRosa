import telebot

def eliminarArticulo(bot, listaArticulos, mensaje):
    codigo = mensaje.text.split()[1]
    if codigo not in listaArticulos:
        bot.reply_to(mensaje, "El articulo especificado no se encuentra en la lista.")
        return
    
    del listaArticulos[codigo]
    bot.reply_to(mensaje, "Articulo eliminado correctamente.")