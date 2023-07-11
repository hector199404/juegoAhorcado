import random
import tkinter as tk

# Lista de palabras para el juego
palabras = ['python', 'programacion', 'desarrollo', 'computadora', 'algoritmo']

def obtener_palabra_aleatoria():
    # Retorna una palabra aleatoria de la lista de palabras
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    # Muestra el estado actual del tablero
    tablero = ''
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + ' '
        else:
            tablero += '_ '
    return tablero

def actualizar_tablero():
    # Actualiza el estado del tablero en la etiqueta
    estado_tablero.set(mostrar_tablero(palabra_secreta, letras_adivinadas))

def adivinar_letra():
    letra = letra_entry.get().lower()
    letra_entry.delete(0, tk.END)

    if letra in letras_adivinadas:
        mensaje.set('¡Ya has adivinado esa letra!')
    elif letra in palabra_secreta:
        letras_adivinadas.append(letra)
        mensaje.set('¡Adivinaste una letra!')
    else:
        intentos.set(intentos.get() - 1)
        mensaje.set('Letra incorrecta. Te quedan {} intentos.'.format(intentos.get()))

    actualizar_tablero()

    if intentos.get() == 0:
        mensaje.set('¡Perdiste! La palabra secreta era: {}'.format(palabra_secreta))
        letra_entry.config(state=tk.DISABLED)
        adivinar_button.config(state=tk.DISABLED)
        adivinar_palabra_button.config(state=tk.DISABLED)

    if all(letra in letras_adivinadas for letra in palabra_secreta):
        mensaje.set('¡Ganaste! Has adivinado la palabra secreta: {}'.format(palabra_secreta))
        letra_entry.config(state=tk.DISABLED)
        adivinar_button.config(state=tk.DISABLED)
        adivinar_palabra_button.config(state=tk.DISABLED)

def adivinar_palabra():
    palabra = letra_entry.get().lower()
    letra_entry.delete(0, tk.END)

    if palabra == palabra_secreta:
        mensaje.set('¡Ganaste! Has adivinado la palabra secreta: {}'.format(palabra_secreta))
        letra_entry.config(state=tk.DISABLED)
        adivinar_button.config(state=tk.DISABLED)
        adivinar_palabra_button.config(state=tk.DISABLED)
    else:
        intentos.set(intentos.get() - 1)
        mensaje.set('Palabra incorrecta. Te quedan {} intentos.'.format(intentos.get()))

        if intentos.get() == 0:
            mensaje.set('¡Perdiste! La palabra secreta era: {}'.format(palabra_secreta))
            letra_entry.config(state=tk.DISABLED)
            adivinar_button.config(state=tk.DISABLED)
            adivinar_palabra_button.config(state=tk.DISABLED)

def comenzar_nuevo_juego():
    global palabra_secreta, letras_adivinadas

    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos.set(6)
    estado_tablero.set(mostrar_tablero(palabra_secreta, letras_adivinadas))
    mensaje.set('¡Bienvenido al juego del Ahorcado!')
    letra_entry.config(state=tk.NORMAL)
    adivinar_button.config(state=tk.NORMAL)
    adivinar_palabra_button.config(state=tk.NORMAL)
    letra_entry.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title('Juego del Ahorcado')

# Variables
palabra_secreta = obtener_palabra_aleatoria()
letras_adivinadas = []
intentos = tk.IntVar(value=6)
estado_tablero = tk.StringVar(value=mostrar_tablero(palabra_secreta, letras_adivinadas))
mensaje = tk.StringVar(value='¡Bienvenido al juego del Ahorcado!')

# Etiquetas
tablero_label = tk.Label(ventana, textvariable=estado_tablero, font=('Arial', 16))
tablero_label.pack(pady=10)

intentos_label = tk.Label(ventana, text='Intentos restantes: ', font=('Arial', 14))
intentos_label.pack()

intentos_display = tk.Label(ventana, textvariable=intentos, font=('Arial', 14))
intentos_display.pack()

mensaje_label = tk.Label(ventana, textvariable=mensaje, font=('Arial', 14))
mensaje_label.pack(pady=10)

letra_label = tk.Label(ventana, text='Ingresa una letra o palabra: ', font=('Arial', 14))
letra_label.pack()

# Entrada de letra
letra_entry = tk.Entry(ventana, font=('Arial', 14))
letra_entry.pack(pady=5)

# Botones
adivinar_button = tk.Button(ventana, text='Adivinar letra', command=adivinar_letra, font=('Arial', 14))
adivinar_button.pack()

adivinar_palabra_button = tk.Button(ventana, text='Adivinar palabra', command=adivinar_palabra, font=('Arial', 14))
adivinar_palabra_button.pack()

nuevo_juego_button = tk.Button(ventana, text='Comenzar nuevo juego', command=comenzar_nuevo_juego, font=('Arial', 14))
nuevo_juego_button.pack()

# Iniciar el juego
ventana.mainloop()

