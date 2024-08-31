def procesarEdad():
    def validarEdad(edad):
        if edad > 0:
            return edad
        else:
            print("¡Error! La edad debe ser mayor a 0.")
            return None

    def generarMensajeBienvenida(edad):
        if edad >= 18:
            return f"¡Felicidades! Eres mayor de edad con {edad} años."
        else:
            añosFaltantes = 18 - edad
            return f"Te faltan {añosFaltantes} años para ser mayor de edad."

    def determinarGeneracion(edad):
        yearBirth = 2024 - edad
        generaciones = {
            "Generación Alpha": [2013, 2028],
            "Generación Z": [1997, 2012],
            "Millennial": [1981, 1996],
            "Generación X": [1965, 1980],
            "Baby Boomer": [1946, 1964],
            "Generación Silent": [1928, 1945]
        }
        
        for nombreGeneracion, rango in generaciones.items():
            if rango[0] <= yearBirth <= rango[1]:
                return f"Perteneces a la generación: {nombreGeneracion}"
            
        return "Eres de una generación diferente."

    def roundedEdad(edad):
        if edad % 10 == 0:
            return f"Tu edad de {edad} años es una edad redonda."
        else:
            return f"Tu edad de {edad} años no es una edad redonda."

    def userAge():
        edad = int(input("Por favor, ingresa tu edad: "))
        return validarEdad(edad)

    userInfo = userAge()
    if userInfo is not None:
        welcomeMSG = generarMensajeBienvenida(userInfo)
        genMSG = determinarGeneracion(userInfo)
        roundedAgeMSG = roundedEdad(userInfo)
        print(f"{welcomeMSG}\n{genMSG}\n{roundedAgeMSG}")

procesarEdad()
