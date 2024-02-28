import telebot

def agregarArticulo(bot, listaArticulos, mensaje, log):
    if log == True:
        # Vamos a dividir el mensaje en en palabras para que en un solo mensaje envie codigo, producto, precio, cantidad
        palabras = mensaje.text.split()[1:]
    
        # Verificamos si entregaron los 4 datos para evitar errores mas adelante
        if len(palabras) != 4:
            bot.reply_to(mensaje, "Por favor, proporciona el codigo, nombre, precio, cantidad")
            return
    
        # Como ya verificamos ahora si agregamos // Ojo que ahi son variables que le paso las palabras
        # Ejemplo el usuario envia (1 lechuga 5 1000)
        codigo = palabras[0]  # 1
        articulo = palabras[1]  # lechuga
        precio = palabras[2]  # 5
        cantidad = palabras[3]  # 1000
    
        # Este es un constructor de articulos
        listaArticulos[codigo] = {"articulo": articulo, "precio": precio, "cantidad": cantidad}
        bot.reply_to(mensaje, f"Articulo agregado: {articulo}")
    else:
        bot.reply_to(mensaje, "No iniciaste sesion.")
