
def invitadosApp():
    listaInvitados = []  # Se crea una lista vacía para almacenar los nombres de los invitados.

    def agregarInvitado():
        # Función para agregar invitados a la lista.
        while True:
            nombre = input("Ingrese el nombre del invitado (o presione Enter para terminar): ")
            listaInvitados.append(nombre.capitalize())
            # Agrega el nombre con la primer letra en MAYUS a la lista y muestra un mensaje de confirmación.
            if nombre == "":
                break  # Termina el bucle si el usuario presiona Enter sin ingresar un nombre.
            

    def mostrarInvitados():
        # Función para mostrar todos los invitados en la lista.
        if not listaInvitados:  #Evalúa la lista si la lista esta vacia retorna False y el operador Not
            # revierte el False a True para que el if se ejecute, solamente estaba probrando 
            print("La lista de invitados está vacía.")
        else:
            print("\n📋--> Lista de invitados:")
            for i, invitado in enumerate(listaInvitados):
                print(f"{i + 1} --> {invitado}")  # Muestra el índice y el nombre de cada invitado.

    def mostrarUnInvitado():
        # Función para mostrar un invitado específico basado en el índice.
        mostrarInvitados()
        if listaInvitados:
            indice = int(input("Ingrese el índice del invitado que desea ver: "))
            if 0 <= indice < len(listaInvitados):# Un operacion compuesta(creo), que evalua dos veces una misma variable
                print(f"👤 Invitado: {listaInvitados[indice]}")
                # Muestra el nombre del invitado seleccionado si el índice es válido.
            else:
                print("❌ Índice inválido.")

    def eliminarInvitado():
        # Función para eliminar un invitado de la lista basado en el índice.
        mostrarInvitados()
        if listaInvitados:
            indice = int(input("Ingrese el índice del invitado que desea eliminar: "))
            if 0 <= indice < len(listaInvitados):
                eliminado = listaInvitados.pop(indice)
                print(f"🗑️ {eliminado} ha sido eliminado de la lista.")
                # Elimina el invitado de la lista y muestra un mensaje de confirmación.
            else:
                print("❌ Índice inválido.")

    def buscarInvitado():
        # Función para buscar invitados en la lista por nombre.
        nombre = input("Ingrese el nombre del invitado a buscar: ").capitalize()
        resultados = [i for i, inv in enumerate(listaInvitados) if nombre.lower() in inv.lower()]
        # Busca coincidencias en la lista (sin distinguir entre mayúsculas y minúsculas).
        if resultados:
            print(f"🔍 Resultados de la búsqueda para '{nombre}':")
            for i in resultados:
                print(f"{i}: {listaInvitados[i]}")
                # Muestra los índices y nombres de los invitados que coinciden con la búsqueda.
        else:
            print(f"❌ No se encontraron invitados que coincidan con '{nombre}'.")

    def modificarInvitado():
        # Función para modificar el nombre de un invitado en la lista.
        mostrarInvitados()
        if listaInvitados:
                indice = int(input("Ingrese el índice del invitado que desea modificar: "))
                if 0 <= indice < len(listaInvitados):
                    nuevoNombre = input("Ingrese el nuevo nombre del invitado: ").capitalize()
                    listaInvitados[indice] = nuevoNombre
                    print(f"✏️ El nombre ha sido actualizado a {nuevoNombre}.")
                    # Actualiza el nombre del invitado en la lista y muestra un mensaje de confirmación.
                else:
                    print("❌ Índice inválido.")


    def mostrarMenu():
        # Función para mostrar el menú de opciones.
        print("\n🎉 BIENVENIDO A LA GESTIÓN DE INVITADOS PARA LA FIESTA 🎉")
        print("1. Agregar invitado")
        print("2. Mostrar un invitado")
        print("3. Eliminar invitado")
        print("4. Buscar un invitado")
        print("5. Modificar invitado")
        print("6. Mostrar lista completa")
        print("7. Salir")

    def menu():
        # Función para manejar la selección de opciones del menú.
        # El diccionario asocicia cada opcion a las funciones correspondientes
        opciones = {
            "1": agregarInvitado,
            "2": mostrarUnInvitado,
            "3": eliminarInvitado,
            "4": buscarInvitado,
            "5": modificarInvitado,
            "6": mostrarInvitados
        }
        while True:
            mostrarMenu()
            opcion = input("Seleccione una opción: ")
            if opcion in opciones:
                opciones[opcion]()
                # Llamo correspondiente según la opcion seleccionada
            elif opcion == "7":
                print("\n👋 ¡Gracias por usar el programa!\n")
                break
                # Sale del bucle y termina el programa si se selecciona la opción de salir.
            else:
                print("\n❌ Opción no válida. Por favor, seleccione una opción del 1 al 7.\n")
                # Mensaje de error si la opción seleccionada no es válida.

    menu()

invitadosApp()
# Llama a la función invitadosApp() para iniciar el programa.
