import telebot

# Le estoy entregando: la conexion al bot
# la lista de los productos
# el nombre del producto que vendi
# la cantidad que vendi
def generarVenta(bot, listaArticulos, mensaje):
    palabras = mensaje.text.split()[1:]
    if len(palabras) != 2:
        bot.reply_to(mensaje, "Por favor, dame el nombre del articulo y la cantidad que vendiste.")
        return

    articulo = palabras[0]
    venta = int(palabras[1])

    nombre_articulo = articulo.lower()      # Lower lo que hace es normalizar o comprobar textos ignorando mayusculas y minuslas (tomate === Tomate || tomate === ToMaTe)
    if nombre_articulo in listaArticulos:
        if listaArticulos[nombre_articulo]["cantidad"] >= venta:
            listaArticulos[nombre_articulo]["cantidad"] -= venta
            return f"Venta realizada: Se vendieron {venta} unidades de {nombre_articulo}."
        else:
            return "Lo siento no tengo la cantidad necesaria para cubrir su venta."
    else:
        return "Articulo no encontrado."