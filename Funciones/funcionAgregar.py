import telebot

def agregarArticulo(bot, diccionario, mensaje):
    # Vamos a dividir el mensaje en en palabras para que en un solo mensaje envie codigo, producto, precio, cantidad
    palabras = mensaje.text.split()[1:]
    
    # Verificamos si entregaron los 4 datos para evitar errores mas adelante
    if len(palabras) != 4:
        bot.reply_to(mensaje, "Por favor, proporciona el codigo, nombre, precio, cantidad")
        return
    
    # Como ya verificamos ahora si agregamos // Ojo que ahi son variables que le paso las palabras
    codigo = palabras[0]
    producto = palabras[1]
    precio = palabras[2]
    cantidad = palabras[3]
    
    # Este es un constructor de articulos
    diccionario[codigo] = {"producto": producto, "precio": precio, "cantidad": cantidad}
    bot.reply_to(mensaje, f"Articulo agregado: {producto}")
