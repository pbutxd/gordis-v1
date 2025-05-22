# gordis_v1_avanzado.py

import math
import os
import time
import pyfiglet # ¡Asegúrate de haberlo instalado con: pip install pyfiglet!


# --- Códigos de escape ANSI para colores en la terminal ---
COLOR_ROJO = "\033[91m"
COLOR_VERDE = "\033[92m"
COLOR_AMARILLO = "\033[93m"
COLOR_AZUL = "\033[94m"
COLOR_MAGENTA = "\033[95m"
COLOR_CYAN = "\033[96m"
COLOR_GRIS = "\033[90m" # Un gris para textos secundarios
COLOR_RESET = "\033[0m"

# Aquí está tu logo de la cebra. Ahora está definido DESPUÉS de los colores.
logo_cebra = f"""{COLOR_MAGENTA}
 .  . .  .  . .  .  . .  .  . .  .  .
   .       . 88;t .t. .88S       .    .
     .  .   .   % ;SX    S  .  .   .
 .       .   8 % 88t 8 .;:.          .
   .  .     :     :S:;.  .   .  . .    .
  .    .  .  8   .:::::  : .        .
    . 8t8:888  % ;@88.;@S  8:8:88.    .
  .  .  t %  X;;8:;:;:Xt%@  : ; X  .
      @;8 8; :SSStS%%%.%%. S8 8.S      .
  .   S88888@ X@XXXSXXX8@.888888%   .
         .t     S@@@@@t 8 :....   .
  .      X  888  :::::.8       .     .
    . .XX S% 88 .8888 :8         .    .
  .    8@S.. .S . t  @.8    .  .   .
       ;XS. . St@S   :88.  .         .
  .  .   .    t@ 8t    S;..   .  .
""" + COLOR_RESET

# Constantes físicas (aproximadas para simplicidad)
VELOCIDAD_LUZ_MS = 299792458 # m/s
GRAVEDAD_MS2 = 9.81           # m/s^2 (aceleración de la gravedad en la Tierra)

# Definición de colores para el título ASCII Art (se usarán en ciclo)
COLORES_TITULO = [COLOR_ROJO, COLOR_VERDE, COLOR_AMARILLO, COLOR_AZUL, COLOR_MAGENTA, COLOR_CYAN]

def limpiar_pantalla():
    """Limpia la consola para una mejor visualización del programa."""
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def generar_titulo_gordis():
    """
    Genera el texto 'GORDIS' en ASCII Art con colores.
    Si pyfiglet no está disponible, devuelve un texto simple y una advertencia.
    """
    try:
        gordis_ascii = pyfiglet.figlet_format("GORDIS", font="big")
        lineas = gordis_ascii.split('\n')
        texto_coloreado = []
        for i, linea in enumerate(lineas):
            color = COLORES_TITULO[i % len(COLORES_TITULO)]
            texto_coloreado.append(f"{color}{linea}{COLOR_RESET}")
        return "\n".join(texto_coloreado)
    except Exception as e:
        print(f"{COLOR_ROJO}Advertencia: No se pudo generar el título ASCII (pyfiglet no instalado o error: {e}).{COLOR_RESET}")
        return f"{COLOR_AZUL}--- GORDIS V-1 ---\n¡Tu asistente de matemáticas!{COLOR_RESET}"

def mostrar_menu_principal():
    """Muestra el menú principal de opciones."""
    print(f"\n{COLOR_CYAN}--- ¡Hola! Soy Gordis V-1, tu asistente inteligente. ---{COLOR_RESET}")
    print(f"{COLOR_AMARILLO}Puedes decirme qué quieres hacer (ej: 'Quiero sumar', 'Calcula el seno') o elegir una opción:{COLOR_RESET}")
    print(f"{COLOR_VERDE}1. Operaciones Matemáticas Básicas (+, -, *, /, ^, %, √){COLOR_RESET}")
    print(f"{COLOR_VERDE}2. Funciones Matemáticas Avanzadas (sin, cos, tan, log, factorial){COLOR_RESET}")
    print(f"{COLOR_VERDE}3. Cálculos de Física/Ingeniería (Ohm, Presión, Velocidad, etc.){COLOR_RESET}")
    print(f"{COLOR_MAGENTA}4. Salir{COLOR_RESET}")
    print(f"{COLOR_CYAN}---------------------------------------------------------{COLOR_RESET}")

def mostrar_menu_matematicas_basicas():
    """Muestra el submenú de operaciones matemáticas básicas."""
    print(f"\n{COLOR_AMARILLO}--- Operaciones Matemáticas Básicas ---{COLOR_RESET}")
    print(f"{COLOR_VERDE}1. Suma (+){COLOR_RESET}")
    print(f"{COLOR_VERDE}2. Resta (-){COLOR_RESET}")
    print(f"{COLOR_VERDE}3. Multiplicación (*){COLOR_RESET}")
    print(f"{COLOR_VERDE}4. División (/){COLOR_RESET}")
    print(f"{COLOR_VERDE}5. Potencia (^){COLOR_RESET}")
    print(f"{COLOR_VERDE}6. Raíz Cuadrada (√){COLOR_RESET}")
    print(f"{COLOR_VERDE}7. Módulo (%){COLOR_RESET}")
    print(f"{COLOR_MAGENTA}8. Volver al Menú Principal{COLOR_RESET}")
    print(f"{COLOR_CYAN}----------------------------------------{COLOR_RESET}")

def mostrar_menu_matematicas_avanzadas():
    """Muestra el submenú de funciones matemáticas avanzadas."""
    print(f"\n{COLOR_AMARILLO}--- Funciones Matemáticas Avanzadas ---{COLOR_RESET}")
    print(f"{COLOR_VERDE}1. Seno (sin) - [Grados]{COLOR_RESET}")
    print(f"{COLOR_VERDE}2. Coseno (cos) - [Grados]{COLOR_RESET}")
    print(f"{COLOR_VERDE}3. Tangente (tan) - [Grados]{COLOR_RESET}")
    print(f"{COLOR_VERDE}4. Logaritmo Natural (ln){COLOR_RESET}")
    print(f"{COLOR_VERDE}5. Logaritmo Base 10 (log10){COLOR_RESET}")
    print(f"{COLOR_VERDE}6. Factorial (!){COLOR_RESET}")
    print(f"{COLOR_MAGENTA}7. Volver al Menú Principal{COLOR_RESET}")
    print(f"{COLOR_CYAN}----------------------------------------{COLOR_RESET}")

def mostrar_menu_fisica_ingenieria():
    """Muestra el submenú de cálculos de física/ingeniería."""
    print(f"\n{COLOR_AMARILLO}--- Cálculos de Física/Ingeniería ---{COLOR_RESET}")
    print(f"{COLOR_VERDE}1. Ley de Ohm (V = I * R){COLOR_RESET}")
    print(f"{COLOR_VERDE}2. Presión (P = F / A){COLOR_RESET}")
    print(f"{COLOR_VERDE}3. Velocidad, Distancia, Tiempo (d = v * t){COLOR_RESET}")
    print(f"{COLOR_VERDE}4. Fuerza (F = m * a){COLOR_RESET}")
    print(f"{COLOR_VERDE}5. Energía (E = m * c^2){COLOR_RESET}")
    print(f"{COLOR_VERDE}6. Conversión de Velocidad (m/s <-> km/h){COLOR_RESET}")
    print(f"{COLOR_MAGENTA}7. Volver al Menú Principal{COLOR_RESET}")
    print(f"{COLOR_CYAN}---------------------------------------------{COLOR_RESET}")

def obtener_numero(mensaje):
    """Pide al usuario un número y valida que sea un número flotante."""
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print(f"{COLOR_ROJO}❌ Entrada inválida. Por favor, ingresa un número válido.{COLOR_RESET}")

def realizar_operacion_basica(num1, num2, operacion):
    """Realiza las operaciones matemáticas básicas."""
    if operacion == '+':
        return num1 + num2
    elif operacion == '-':
        return num1 - num2
    elif operacion == '*':
        return num1 * num2
    elif operacion == '/':
        if num2 == 0:
            return f"{COLOR_ROJO}Error: ¡No se puede dividir por cero!{COLOR_RESET}"
        else:
            return num1 / num2
    elif operacion == '^':
        return num1 ** num2
    elif operacion == '√':
        if num1 < 0:
            return f"{COLOR_ROJO}Error: La raíz cuadrada de un número negativo no es un número real.{COLOR_RESET}"
        else:
            return math.sqrt(num1)
    elif operacion == '%':
        if num2 == 0:
            return f"{COLOR_ROJO}Error: ¡No se puede calcular el módulo por cero!{COLOR_RESET}"
        else:
            return num1 % num2
    else:
        return f"{COLOR_ROJO}Operación básica no reconocida.{COLOR_RESET}"

def realizar_operacion_avanzada(num, operacion):
    """Realiza las operaciones matemáticas avanzadas (usan un solo número)."""
    if operacion == 'sin':
        return math.sin(math.radians(num)) # Convertir grados a radianes
    elif operacion == 'cos':
        return math.cos(math.radians(num)) # Convertir grados a radianes
    elif operacion == 'tan':
        # Para evitar problemas con tangentes de ángulos cercanos a 90 o 270 grados
        # donde el coseno es muy cercano a cero, puedes añadir una pequeña tolerancia
        if abs(math.cos(math.radians(num))) < 1e-9: # 1e-9 es 0.000000001
             return f"{COLOR_ROJO}Error: Tangente indefinida (coseno de 0).{COLOR_RESET}"
        return math.tan(math.radians(num)) # Convertir grados a radianes
    elif operacion == 'ln':
        if num <= 0:
            return f"{COLOR_ROJO}Error: Logaritmo natural solo para números positivos.{COLOR_RESET}"
        return math.log(num)
    elif operacion == 'log10':
        if num <= 0:
            return f"{COLOR_ROJO}Error: Logaritmo base 10 solo para números positivos.{COLOR_RESET}"
        return math.log10(num)
    elif operacion == '!':
        if num < 0 or not num.is_integer():
            return f"{COLOR_ROJO}Error: Factorial solo para enteros no negativos.{COLOR_RESET}"
        return math.factorial(int(num)) # factorial necesita un entero
    else:
        return f"{COLOR_ROJO}Operación avanzada no reconocida.{COLOR_RESET}"

def realizar_calculo_fisica_ingenieria(sub_eleccion):
    """Gestiona los cálculos de física/ingeniería."""
    global contador_operaciones # Para poder incrementar el contador global

    if sub_eleccion == 1: # Ley de Ohm
        print(f"\n{COLOR_AMARILLO}--- Ley de Ohm (V=IR) ---{COLOR_RESET}")
        print(f"{COLOR_GRIS}Unidades: Voltios (V), Amperios (A), Ohmios (Ω){COLOR_RESET}")
        print(f"{COLOR_GRIS}Elige qué calcular: {COLOR_RESET}")
        print(f"{COLOR_VERDE}a. Voltaje (V){COLOR_RESET}")
        print(f"{COLOR_VERDE}b. Corriente (I){COLOR_RESET}")
        print(f"{COLOR_VERDE}c. Resistencia (R){COLOR_RESET}")
        calc_ohm = input(f"{COLOR_AZUL}👉 Opción (a/b/c): {COLOR_RESET}").lower().strip()

        if calc_ohm == 'a': # Calcular Voltaje (V = I * R)
            I = obtener_numero(f"{COLOR_AZUL}Ingresa Corriente (Amperios): {COLOR_RESET}")
            R = obtener_numero(f"{COLOR_AZUL}Ingresa Resistencia (Ohmios): {COLOR_RESET}")
            resultado = I * R
            print(f"\n{COLOR_VERDE}✨ El Voltaje (V) es: {resultado:.2f} V{COLOR_RESET}")
        elif calc_ohm == 'b': # Calcular Corriente (I = V / R)
            V = obtener_numero(f"{COLOR_AZUL}Ingresa Voltaje (Voltios): {COLOR_RESET}")
            R = obtener_numero(f"{COLOR_AZUL}Ingresa Resistencia (Ohmios): {COLOR_RESET}")
            if R == 0: resultado = f"{COLOR_ROJO}Error: Resistencia no puede ser cero.{COLOR_RESET}"
            else: resultado = V / R
            print(f"\n{COLOR_VERDE}✨ La Corriente (I) es: {resultado:.2f} A{COLOR_RESET}")
        elif calc_ohm == 'c': # Calcular Resistencia (R = V / I)
            V = obtener_numero(f"{COLOR_AZUL}Ingresa Voltaje (Voltios): {COLOR_RESET}")
            I = obtener_numero(f"{COLOR_AZUL}Ingresa Corriente (Amperios): {COLOR_RESET}")
            if I == 0: resultado = f"{COLOR_ROJO}Error: Corriente no puede ser cero.{COLOR_RESET}"
            else: resultado = V / I
            print(f"\n{COLOR_VERDE}✨ La Resistencia (R) es: {resultado:.2f} Ω{COLOR_RESET}")
        else:
            print(f"{COLOR_ROJO}Opción no válida para Ley de Ohm.{COLOR_RESET}")
            resultado = "Error" # Marcar como error para no contar

    elif sub_eleccion == 2: # Presión (P = F / A)
        print(f"\n{COLOR_AMARILLO}--- Presión (P=F/A) ---{COLOR_RESET}")
        print(f"{COLOR_GRIS}Unidades: Presión (Pascales, Pa), Fuerza (Newtons, N), Área (metros cuadrados, m²){COLOR_RESET}")
        F = obtener_numero(f"{COLOR_AZUL}Ingresa la Fuerza (Newtons): {COLOR_RESET}")
        A = obtener_numero(f"{COLOR_AZUL}Ingresa el Área (metros cuadrados): {COLOR_RESET}")
        if A == 0: resultado = f"{COLOR_ROJO}Error: El área no puede ser cero.{COLOR_RESET}"
        else: resultado = F / A
        print(f"\n{COLOR_VERDE}✨ La Presión (P) es: {resultado:.2f} Pa{COLOR_RESET}")
    
    elif sub_eleccion == 3: # Velocidad, Distancia, Tiempo (d = v * t)
        print(f"\n{COLOR_AMARILLO}--- Velocidad, Distancia, Tiempo ---{COLOR_RESET}")
        print(f"{COLOR_GRIS}Unidades: Distancia (metros, m), Velocidad (m/s), Tiempo (segundos, s){COLOR_RESET}")
        print(f"{COLOR_GRIS}Elige qué calcular: {COLOR_RESET}")
        print(f"{COLOR_VERDE}a. Distancia (d){COLOR_RESET}")
        print(f"{COLOR_VERDE}b. Velocidad (v){COLOR_RESET}")
        print(f"{COLOR_VERDE}c. Tiempo (t){COLOR_RESET}")
        calc_vdt = input(f"{COLOR_AZUL}👉 Opción (a/b/c): {COLOR_RESET}").lower().strip()

        if calc_vdt == 'a': # Calcular Distancia (d = v * t)
            v = obtener_numero(f"{COLOR_AZUL}Ingresa la Velocidad (m/s): {COLOR_RESET}")
            t = obtener_numero(f"{COLOR_AZUL}Ingresa el Tiempo (segundos): {COLOR_RESET}")
            resultado = v * t
            print(f"\n{COLOR_VERDE}✨ La Distancia (d) es: {resultado:.2f} m{COLOR_RESET}")
        elif calc_vdt == 'b': # Calcular Velocidad (v = d / t)
            d = obtener_numero(f"{COLOR_AZUL}Ingresa la Distancia (metros): {COLOR_RESET}")
            t = obtener_numero(f"{COLOR_AZUL}Ingresa el Tiempo (segundos): {COLOR_RESET}")
            if t == 0: resultado = f"{COLOR_ROJO}Error: El tiempo no puede ser cero.{COLOR_RESET}"
            else: resultado = d / t
            print(f"\n{COLOR_VERDE}✨ La Velocidad (v) es: {resultado:.2f} m/s{COLOR_RESET}")
        elif calc_vdt == 'c': # Calcular Tiempo (t = d / v)
            d = obtener_numero(f"{COLOR_AZUL}Ingresa la Distancia (metros): {COLOR_RESET}")
            v = obtener_numero(f"{COLOR_AZUL}Ingresa la Velocidad (m/s): {COLOR_RESET}")
            if v == 0: resultado = f"{COLOR_ROJO}Error: La velocidad no puede ser cero.{COLOR_RESET}"
            else: resultado = d / v
            print(f"\n{COLOR_VERDE}✨ El Tiempo (t) es: {resultado:.2f} s{COLOR_RESET}")
        else:
            print(f"{COLOR_ROJO}Opción no válida para Velocidad, Distancia, Tiempo.{COLOR_RESET}")
            resultado = "Error" # Marcar como error para no contar

    elif sub_eleccion == 4: # Fuerza (F = m * a)
        print(f"\n{COLOR_AMARILLO}--- Fuerza (F=ma) ---{COLOR_RESET}")
        print(f"{COLOR_GRIS}Unidades: Fuerza (Newtons, N), Masa (kilogramos, kg), Aceleración (m/s²){COLOR_RESET}")
        m = obtener_numero(f"{COLOR_AZUL}Ingresa la Masa (kg): {COLOR_RESET}")
        a = obtener_numero(f"{COLOR_AZUL}Ingresa la Aceleración (m/s²): {COLOR_RESET}")
        resultado = m * a
        print(f"\n{COLOR_VERDE}✨ La Fuerza (F) es: {resultado:.2f} N{COLOR_RESET}")
    
    elif sub_eleccion == 5: # Energía (E = mc^2)
        print(f"\n{COLOR_AMARILLO}--- Energía (E=mc²) ---{COLOR_RESET}")
        print(f"{COLOR_GRIS}Unidades: Energía (Julios, J), Masa (kilogramos, kg), c (m/s){COLOR_RESET}")
        print(f"{COLOR_GRIS}Velocidad de la luz (c) = {VELOCIDAD_LUZ_MS} m/s (constante){COLOR_RESET}")
        m = obtener_numero(f"{COLOR_AZUL}Ingresa la Masa (kg): {COLOR_RESET}")
        resultado = m * (VELOCIDAD_LUZ_MS ** 2)
        print(f"\n{COLOR_VERDE}✨ La Energía (E) es: {resultado:.2e} J{COLOR_RESET}") # .2e para notación científica
    
    elif sub_eleccion == 6: # Conversión de Velocidad
        print(f"\n{COLOR_AMARILLO}--- Conversión de Velocidad ---{COLOR_RESET}")
        print(f"{COLOR_VERDE}1. m/s a km/h{COLOR_RESET}")
        print(f"{COLOR_VERDE}2. km/h a m/s{COLOR_RESET}")
        tipo_conversion = input(f"{COLOR_AZUL}👉 Opción (1/2): {COLOR_RESET}").strip()
        valor = obtener_numero(f"{COLOR_AZUL}Ingresa el valor a convertir: {COLOR_RESET}")

        if tipo_conversion == '1':
            resultado = valor * 3.6 # m/s * 3.6 = km/h
            print(f"\n{COLOR_VERDE}✨ {valor} m/s son: {resultado:.2f} km/h{COLOR_RESET}")
        elif tipo_conversion == '2':
            resultado = valor / 3.6 # km/h / 3.6 = m/s
            print(f"\n{COLOR_VERDE}✨ {valor} km/h son: {resultado:.2f} m/s{COLOR_RESET}")
        else:
            print(f"{COLOR_ROJO}Opción de conversión no válida.{COLOR_RESET}")
            resultado = "Error" # Marcar como error para no contar
    else:
        print(f"{COLOR_ROJO}Opción de cálculo de Física/Ingeniería no válida.{COLOR_RESET}")
        return "Error" # Marcar como error para no contar

    # Cuenta la operación solo si no fue un error
    if not isinstance(resultado, str) or not resultado.startswith(COLOR_ROJO + "Error"):
        contador_operaciones += 1
    
    return resultado # Devuelve el resultado (o error)

# --- Bloque Principal del Programa ---
if __name__ == "__main__":
    limpiar_pantalla()
    print(generar_titulo_gordis())
    # *** Aquí es donde se imprime tu logo de la cebra ***
    print(logo_cebra)
    time.sleep(2) # Damos un poco más de tiempo para apreciar el logo y el título
    limpiar_pantalla()

    nombre_usuario = input(f"{COLOR_AZUL}¡Hola! ¿Cómo te llamas? {COLOR_RESET}").strip()
    if nombre_usuario:
        print(f"{COLOR_VERDE}¡Qué bien verte, {nombre_usuario}! Gordis V-1 está listo para tus cálculos.{COLOR_RESET}\n")
    else:
        print(f"{COLOR_VERDE}¡Qué bien verte! Gordis V-1 está listo para tus cálculos.{COLOR_RESET}\n")
    time.sleep(1)

    contador_operaciones = 0

    while True:
        limpiar_pantalla()
        mostrar_menu_principal() # Muestra el menú principal

        # *** CAMBIOS PARA EL MODO CHATBOX BÁSICO ***
        eleccion_principal = input(f"{COLOR_AZUL}👉 ¿Qué quieres hacer hoy (ej: 'sumar', 'seno 30', 'salir') o elige un número?: {COLOR_RESET}").strip().lower() # Convertir a minúsculas

        # Easter Egg
        if eleccion_principal == 'gordis':
            print(f"{COLOR_MAGENTA}💬 ¡Soy Gordis! Me alegra que pienses en mí. Ahora, dime qué cálculo necesitas o elige una opción.{COLOR_RESET}")
            time.sleep(1.5)
            continue
        
        # --- Lógica de procesamiento de palabras clave ---
        operacion_reconocida = False

        # Matemáticas Básicas
        if "suma" in eleccion_principal or "+" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, una suma. Dime los números...{COLOR_RESET}\n")
            num1 = obtener_numero(f"{COLOR_AZUL}Ingresa el primer número: {COLOR_RESET}")
            num2 = obtener_numero(f"{COLOR_AZUL}Ingresa el segundo número: {COLOR_RESET}")
            resultado = realizar_operacion_basica(num1, num2, '+')
            print(f"\n{COLOR_VERDE}✨ El resultado de {num1} + {num2} es: {resultado}{COLOR_RESET}")
            operacion_reconocida = True
        elif "resta" in eleccion_principal or "-" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, una resta. Dime los números...{COLOR_RESET}\n")
            num1 = obtener_numero(f"{COLOR_AZUL}Ingresa el primer número: {COLOR_RESET}")
            num2 = obtener_numero(f"{COLOR_AZUL}Ingresa el segundo número: {COLOR_RESET}")
            resultado = realizar_operacion_basica(num1, num2, '-')
            print(f"\n{COLOR_VERDE}✨ El resultado de {num1} - {num2} es: {resultado}{COLOR_RESET}")
            operacion_reconocida = True
        elif "multiplicacion" in eleccion_principal or "*" in eleccion_principal or "multiplicar" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, una multiplicación. Dime los números...{COLOR_RESET}\n")
            num1 = obtener_numero(f"{COLOR_AZUL}Ingresa el primer número: {COLOR_RESET}")
            num2 = obtener_numero(f"{COLOR_AZUL}Ingresa el segundo número: {COLOR_RESET}")
            resultado = realizar_operacion_basica(num1, num2, '*')
            print(f"\n{COLOR_VERDE}✨ El resultado de {num1} * {num2} es: {resultado}{COLOR_RESET}")
            operacion_reconocida = True
        elif "division" in eleccion_principal or "/" in eleccion_principal or "dividir" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, una división. Dime los números...{COLOR_RESET}\n")
            num1 = obtener_numero(f"{COLOR_AZUL}Ingresa el primer número: {COLOR_RESET}")
            num2 = obtener_numero(f"{COLOR_AZUL}Ingresa el segundo número: {COLOR_RESET}")
            resultado = realizar_operacion_basica(num1, num2, '/')
            print(f"\n{COLOR_VERDE}✨ El resultado de {num1} / {num2} es: {resultado}{COLOR_RESET}")
            operacion_reconocida = True
        elif "potencia" in eleccion_principal or "^" in eleccion_principal or "elevar" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, una potencia. Dime la base y el exponente...{COLOR_RESET}\n")
            num1 = obtener_numero(f"{COLOR_AZUL}Ingresa la base: {COLOR_RESET}")
            num2 = obtener_numero(f"{COLOR_AZUL}Ingresa el exponente: {COLOR_RESET}")
            resultado = realizar_operacion_basica(num1, num2, '^')
            print(f"\n{COLOR_VERDE}✨ El resultado de {num1}^{num2} es: {resultado}{COLOR_RESET}")
            operacion_reconocida = True
        elif "raiz" in eleccion_principal or "raíz" in eleccion_principal or "√" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, una raíz cuadrada. Dime el número...{COLOR_RESET}\n")
            num1 = obtener_numero(f"{COLOR_AZUL}Ingresa el número para calcular la raíz cuadrada: {COLOR_RESET}")
            resultado = realizar_operacion_basica(num1, 0, '√')
            print(f"\n{COLOR_VERDE}✨ El resultado de √{num1} es: {resultado}{COLOR_RESET}")
            operacion_reconocida = True
        elif "modulo" in eleccion_principal or "%" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, un módulo. Dime los números...{COLOR_RESET}\n")
            num1 = obtener_numero(f"{COLOR_AZUL}Ingresa el dividendo: {COLOR_RESET}")
            num2 = obtener_numero(f"{COLOR_AZUL}Ingresa el divisor: {COLOR_RESET}")
            resultado = realizar_operacion_basica(num1, num2, '%')
            print(f"\n{COLOR_VERDE}✨ El resultado de {num1} % {num2} es: {resultado}{COLOR_RESET}")
            operacion_reconocida = True

        # Matemáticas Avanzadas (solo una operación por ahora, para ejemplificar)
        elif "seno" in eleccion_principal or "sin" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, cálculo de seno. Dime el ángulo en grados...{COLOR_RESET}\n")
            num = obtener_numero(f"{COLOR_AZUL}Ingresa el ángulo en grados: {COLOR_RESET}")
            resultado = realizar_operacion_avanzada(num, 'sin')
            print(f"\n{COLOR_VERDE}✨ El Seno de {num}° es: {resultado}{COLOR_RESET}")
            operacion_reconocida = True
        elif "coseno" in eleccion_principal or "cos" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, cálculo de coseno. Dime el ángulo en grados...{COLOR_RESET}\n")
            num = obtener_numero(f"{COLOR_AZUL}Ingresa el ángulo en grados: {COLOR_RESET}")
            resultado = realizar_operacion_avanzada(num, 'cos')
            print(f"\n{COLOR_VERDE}✨ El Coseno de {num}° es: {resultado}{COLOR_RESET}")
            operacion_reconocida = True
        elif "tangente" in eleccion_principal or "tan" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, cálculo de tangente. Dime el ángulo en grados...{COLOR_RESET}\n")
            num = obtener_numero(f"{COLOR_AZUL}Ingresa el ángulo en grados: {COLOR_RESET}")
            resultado = realizar_operacion_avanzada(num, 'tan')
            print(f"\n{COLOR_VERDE}✨ La Tangente de {num}° es: {resultado}{COLOR_RESET}")
            operacion_reconocida = True
        elif "logaritmo natural" in eleccion_principal or "ln" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, cálculo de logaritmo natural. Dime el número...{COLOR_RESET}\n")
            num = obtener_numero(f"{COLOR_AZUL}Ingresa el número: {COLOR_RESET}")
            resultado = realizar_operacion_avanzada(num, 'ln')
            print(f"\n{COLOR_VERDE}✨ El Logaritmo Natural de {num} es: {resultado}{COLOR_RESET}")
            operacion_reconocida = True
        elif "logaritmo base 10" in eleccion_principal or "log10" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, cálculo de logaritmo base 10. Dime el número...{COLOR_RESET}\n")
            num = obtener_numero(f"{COLOR_AZUL}Ingresa el número: {COLOR_RESET}")
            resultado = realizar_operacion_avanzada(num, 'log10')
            print(f"\n{COLOR_VERDE}✨ El Logaritmo Base 10 de {num} es: {resultado}{COLOR_RESET}")
            operacion_reconocida = True
        elif "factorial" in eleccion_principal or "!" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, cálculo de factorial. Dime el número entero no negativo...{COLOR_RESET}\n")
            num = obtener_numero(f"{COLOR_AZUL}Ingresa el número: {COLOR_RESET}")
            resultado = realizar_operacion_avanzada(num, '!')
            print(f"\n{COLOR_VERDE}✨ El Factorial de {int(num)} es: {resultado}{COLOR_RESET}")
            operacion_reconocida = True

        # Cálculos de Física/Ingeniería (solo uno para ejemplificar)
        elif "ohm" in eleccion_principal or "ley de ohm" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, Ley de Ohm. Dime qué quieres calcular (Voltaje, Corriente, Resistencia)...{COLOR_RESET}\n")
            # Llamamos directamente a la función, que ya maneja su propio sub-menú de preguntas
            realizar_calculo_fisica_ingenieria(1) # 1 corresponde a Ley de Ohm en el menú de física
            operacion_reconocida = True
        elif "presion" in eleccion_principal or "presión" in eleccion_principal or "fuerza area" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, cálculo de Presión. Dime la fuerza y el área...{COLOR_RESET}\n")
            realizar_calculo_fisica_ingenieria(2)
            operacion_reconocida = True
        elif "velocidad" in eleccion_principal or "distancia" in eleccion_principal or "tiempo" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, cálculo de Velocidad, Distancia o Tiempo. Dime qué quieres calcular...{COLOR_RESET}\n")
            realizar_calculo_fisica_ingenieria(3)
            operacion_reconocida = True
        elif "fuerza" in eleccion_principal and "masa" in eleccion_principal: # Para diferenciar de 'fuerza area'
            print(f"{COLOR_AMARILLO}🚀 Entendido, cálculo de Fuerza. Dime la masa y la aceleración...{COLOR_RESET}\n")
            realizar_calculo_fisica_ingenieria(4)
            operacion_reconocida = True
        elif "energia" in eleccion_principal or "energía" in eleccion_principal or "emc2" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, cálculo de Energía (E=mc²). Dime la masa...{COLOR_RESET}\n")
            realizar_calculo_fisica_ingenieria(5)
            operacion_reconocida = True
        elif "convertir velocidad" in eleccion_principal or "velocidad conversion" in eleccion_principal or "kmh" in eleccion_principal or "m/s" in eleccion_principal:
            print(f"{COLOR_AMARILLO}🚀 Entendido, conversión de velocidad. Dime el valor y qué tipo de conversión...{COLOR_RESET}\n")
            realizar_calculo_fisica_ingenieria(6)
            operacion_reconocida = True


        if operacion_reconocida:
            input(f"\n{COLOR_CYAN}Presiona Enter para continuar...{COLOR_RESET}")
            continue # Vuelve al inicio del bucle principal después de una operación por chat
        # --- Fin de la lógica de procesamiento de palabras clave ---

        # Si no se reconoció una palabra clave, intenta interpretar como número de menú
        if not eleccion_principal.isdigit():
            print(f"{COLOR_ROJO}🤔 No te entendí. Por favor, sé más específico o ingresa un número de opción (1-4).{COLOR_RESET}")
            time.sleep(1.5)
            continue

        eleccion_principal_num = int(eleccion_principal)

        if eleccion_principal_num == 4: # Salir del programa
            limpiar_pantalla()
            print(f"{COLOR_MAGENTA}👋 ¡Adiós! Fue un placer ayudarte con tus cálculos. ¡Hasta la próxima!{COLOR_RESET}")
            print(f"{COLOR_AMARILLO}📈 Realizaste {contador_operaciones} operaciones en esta sesión.{COLOR_RESET}")
            time.sleep(2)
            break
        elif eleccion_principal_num == 1: # Matemáticas Básicas
            while True: # Sub-bucle para matemáticas básicas
                limpiar_pantalla()
                mostrar_menu_matematicas_basicas()
                sub_eleccion = input(f"{COLOR_AZUL}👉 Ingresa tu elección (1-8): {COLOR_RESET}").strip()

                if not sub_eleccion.isdigit():
                    print(f"{COLOR_ROJO}🤔 Entrada no válida. Por favor, ingresa un número de opción (1-8).{COLOR_RESET}")
                    time.sleep(1.5)
                    continue
                
                sub_eleccion_num = int(sub_eleccion)

                if sub_eleccion_num == 8: # Volver al Menú Principal
                    print(f"{COLOR_GRIS}Volviendo al menú principal...{COLOR_RESET}")
                    time.sleep(1)
                    break # Sale del sub-bucle y vuelve al bucle principal
                elif 1 <= sub_eleccion_num <= 7:
                    print(f"{COLOR_AMARILLO}🚀 Preparando la operación...{COLOR_RESET}\n")

                    operacion_simbolo = ''
                    if sub_eleccion_num == 1: operacion_simbolo = '+'
                    elif sub_eleccion_num == 2: operacion_simbolo = '-'
                    elif sub_eleccion_num == 3: operacion_simbolo = '*'
                    elif sub_eleccion_num == 4: operacion_simbolo = '/'
                    elif sub_eleccion_num == 5: operacion_simbolo = '^'
                    elif sub_eleccion_num == 7: operacion_simbolo = '%'
                    
                    if sub_eleccion_num == 6: # Raíz Cuadrada (solo un número)
                        num1 = obtener_numero(f"{COLOR_AZUL}Ingresa el número para calcular la raíz cuadrada: {COLOR_RESET}")
                        resultado = realizar_operacion_basica(num1, 0, '√')
                        print(f"\n{COLOR_VERDE}✨ El resultado de √{num1} es: {resultado}{COLOR_RESET}")
                    else: # Operaciones con dos números
                        num1 = obtener_numero(f"{COLOR_AZUL}Ingresa el primer número: {COLOR_RESET}")
                        num2 = obtener_numero(f"{COLOR_AZUL}Ingresa el segundo número: {COLOR_RESET}")
                        resultado = realizar_operacion_basica(num1, num2, operacion_simbolo)
                        print(f"\n{COLOR_VERDE}✨ El resultado de {num1} {operacion_simbolo} {num2} es: {resultado}{COLOR_RESET}")
                    
                    if not isinstance(resultado, str) or not resultado.startswith(COLOR_ROJO + "Error"):
                        contador_operaciones += 1
                    
                    input(f"\n{COLOR_CYAN}Presiona Enter para continuar...{COLOR_RESET}")
                else:
                    print(f"{COLOR_ROJO}🤔 Opción no válida. Por favor, elige un número del 1 al 8.{COLOR_RESET}")
                    time.sleep(1.5)

        elif eleccion_principal_num == 2: # Matemáticas Avanzadas
            while True: # Sub-bucle para matemáticas avanzadas
                limpiar_pantalla()
                mostrar_menu_matematicas_avanzadas()
                sub_eleccion = input(f"{COLOR_AZUL}👉 Ingresa tu elección (1-7): {COLOR_RESET}").strip()

                if not sub_eleccion.isdigit():
                    print(f"{COLOR_ROJO}🤔 Entrada no válida. Por favor, ingresa un número de opción (1-7).{COLOR_RESET}")
                    time.sleep(1.5)
                    continue
                
                sub_eleccion_num = int(sub_eleccion)

                if sub_eleccion_num == 7: # Volver al Menú Principal
                    print(f"{COLOR_GRIS}Volviendo al menú principal...{COLOR_RESET}")
                    time.sleep(1)
                    break # Sale del sub-bucle
                elif 1 <= sub_eleccion_num <= 6:
                    print(f"{COLOR_AMARILLO}🚀 Preparando la operación...{COLOR_RESET}\n")
                    
                    operacion_simbolo = ''
                    mensaje_num = ""
                    if sub_eleccion_num == 1: operacion_simbolo = 'sin'; mensaje_num = "ángulo en grados"
                    elif sub_eleccion_num == 2: operacion_simbolo = 'cos'; mensaje_num = "ángulo en grados"
                    elif sub_eleccion_num == 3: operacion_simbolo = 'tan'; mensaje_num = "ángulo en grados"
                    elif sub_eleccion_num == 4: operacion_simbolo = 'ln'; mensaje_num = "número"
                    elif sub_eleccion_num == 5: operacion_simbolo = 'log10'; mensaje_num = "número"
                    elif sub_eleccion_num == 6: operacion_simbolo = '!'; mensaje_num = "entero no negativo"

                    num = obtener_numero(f"{COLOR_AZUL}Ingresa el {mensaje_num}: {COLOR_RESET}")
                    resultado = realizar_operacion_avanzada(num, operacion_simbolo)
                    
                    if operacion_simbolo == '!':
                        print(f"\n{COLOR_VERDE}✨ El Factorial de {int(num)} es: {resultado}{COLOR_RESET}")
                    else:
                        print(f"\n{COLOR_VERDE}✨ El resultado de {operacion_simbolo}({num}) es: {resultado}{COLOR_RESET}")
                    
                    if not isinstance(resultado, str) or not resultado.startswith(COLOR_ROJO + "Error"):
                        contador_operaciones += 1
                    
                    input(f"\n{COLOR_CYAN}Presiona Enter para continuar...{COLOR_RESET}")
                else:
                    print(f"{COLOR_ROJO}🤔 Opción no válida. Por favor, elige un número del 1 al 7.{COLOR_RESET}")
                    time.sleep(1.5)

        elif eleccion_principal_num == 3: # Cálculos de Física/Ingeniería
            while True: # Sub-bucle para física/ingeniería
                limpiar_pantalla()
                mostrar_menu_fisica_ingenieria()
                sub_eleccion = input(f"{COLOR_AZUL}👉 Ingresa tu elección (1-7): {COLOR_RESET}").strip()

                if not sub_eleccion.isdigit():
                    print(f"{COLOR_ROJO}🤔 Entrada no válida. Por favor, ingresa un número de opción (1-7).{COLOR_RESET}")
                    time.sleep(1.5)
                    continue
                
                sub_eleccion_num = int(sub_eleccion)

                if sub_eleccion_num == 7: # Volver al Menú Principal
                    print(f"{COLOR_GRIS}Volviendo al menú principal...{COLOR_RESET}")
                    time.sleep(1)
                    break # Sale del sub-bucle
                elif 1 <= sub_eleccion_num <= 6:
                    print(f"{COLOR_AMARILLO}🚀 Preparando cálculo...{COLOR_RESET}\n")
                    # La función 'realizar_calculo_fisica_ingenieria' ya maneja la cuenta y el mensaje
                    resultado_fisica = realizar_calculo_fisica_ingenieria(sub_eleccion_num)
                    
                    input(f"\n{COLOR_CYAN}Presiona Enter para continuar...{COLOR_RESET}")
                else:
                    print(f"{COLOR_ROJO}🤔 Opción no válida. Por favor, elige un número del 1 al 7.{COLOR_RESET}")
                    time.sleep(1.5)
        else:
            print(f"{COLOR_ROJO}🤔 Opción no válida. Por favor, elige un número del 1 al 4.{COLOR_RESET}")
            time.sleep(1.5)
