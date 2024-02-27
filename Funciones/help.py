import telebot
 
class COMANDOS:
    Agregar = "/Agregar"
    Editar = "/Editar"
    Eliminar = "/Eliminar"
    Ver = "/Ver"

def helper(bot, mensaje):
     bot.reply_to(mensaje, f"""🤖 Hola, soy el Bot Tiendita rosita le ayudara con su tienda.\n
    Se puede comunicar conmigo a traves de los siguentes comandos:\n
    {COMANDOS.Agregar} (Con esto agregas tus productos, aqui un ejemplo: Agregar 1 lechuga 5 1000).\n
    {COMANDOS.Editar} (Con esto editaras un producto.).\n
    {COMANDOS.Eliminar} (Con esto eliminaras un producto).\n
    {COMANDOS.Ver} (Con esto veras todos los productos que tienes en tu tiendita.).
    """)