def procesarEdad():
    # Función para validar si la edad ingresada es mayor a 0.
    def validarEdad(edad):
        if edad > 0:  # Verifica que la edad sea mayor que 0.
            return edad  # Si es válida, retorna la edad.
        else:
            print("¡Error! La edad debe ser mayor a 0.")  # Mensaje de error si la edad no es válida.
            return None  # Retorna None si la edad no es válida.

    # Función para generar un mensaje de bienvenida basado en la edad.
    def generarMensajeBienvenida(edad):
        if edad >= 18:  # Verifica si la persona es mayor de edad.
            return f"¡Felicidades! Eres mayor de edad con {edad} años."
        else:
            añosFaltantes = 18 - edad  # Calcula los años faltantes para llegar a los 18.
            return f"Te faltan {añosFaltantes} años para ser mayor de edad."

    # Función para determinar a qué generación pertenece la persona según su edad.
    def determinarGeneracion(edad):
        yearBirth = 2024 - edad  # Calcula el año de nacimiento basado en la edad.
        generaciones = {
            "Generación Alpha": [2013, 2028],
            "Generación Z": [1997, 2012],
            "Millennial": [1981, 1996],
            "Generación X": [1965, 1980],
            "Baby Boomer": [1946, 1964],
            "Generación Silent": [1928, 1945]
        }
        
        # Recorre cada generación para encontrar cuál coincide con el año de nacimiento.
        for nombreGeneracion, rango in generaciones.items():
            if rango[0] <= yearBirth <= rango[1]:  # Verifica si el año de nacimiento está dentro del rango de la generación.
                return f"Perteneces a la generación: {nombreGeneracion}"
        
        return "Eres de una generación diferente."  # Mensaje si el año de nacimiento no encaja en las generaciones definidas.

    # Función para verificar si la edad ingresada es un número redondo (múltiplo de 10).
    def roundedEdad(edad):
        if edad % 10 == 0:  # Verifica si la edad es un múltiplo de 10.
            return f"Tu edad de {edad} años es una edad redonda."
        else:
            return f"Tu edad de {edad} años no es una edad redonda."

    # Función principal para solicitar la edad del usuario y procesarla.
    def userAge():
        edad = int(input("Por favor, ingresa tu edad: "))  # Solicita al usuario que ingrese su edad.
        return validarEdad(edad)  # Valida la edad ingresada.

    userInfo = userAge()  # Llama a la función para obtener y validar la edad del usuario.
    if userInfo is not None:  # Verifica que la edad sea válida (no None).
        welcomeMSG = generarMensajeBienvenida(userInfo)  # Genera un mensaje de bienvenida.
        genMSG = determinarGeneracion(userInfo)  # Determina la generación del usuario.
        roundedAgeMSG = roundedEdad(userInfo)  # Verifica si la edad es un número redondo.
        print(f"{welcomeMSG}\n{genMSG}\n{roundedAgeMSG}")  # Imprime todos los mensajes generados.

procesarEdad()
