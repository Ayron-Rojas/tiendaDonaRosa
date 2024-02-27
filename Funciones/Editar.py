import telebot

def editarArticulo(bot, listaArticulos, mensaje):
    palabras = mensaje.text.split()[1:]
    
    if len(palabras) != 4:
        bot.reply_to(mensaje, "Por favor, proporciona el codigo de la fruta seguido del nuevo nombre, precio y cantidad")
        return
    
    codigo = palabras[0]
    if codigo not in listaArticulos:
        bot.reply_to(mensaje, "El articulo especificado no esta en la lista.")
        return
    
    articulo = palabras[1]
    precio = float(palabras[2])
    cantidad = int(palabras[3])
    
    listaArticulos[codigo] = {'articulo': articulo, 'precio': precio, 'cantidad': cantidad}
    bot.reply_to(mensaje, f"Articulo editado: {articulo}")