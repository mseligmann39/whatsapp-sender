from sender import send_whatsapp_message

if __name__ == "__main__":
    numero = ""  # Número con prefijo internacional
    mensaje = "¡Hola! Este es un mensaje de prueba automatizado para un test.\nSegundo parrafo\n Tercer parrafo, tengo caca"
    send_whatsapp_message(numero, mensaje)
    