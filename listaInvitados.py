def invitadosApp():
    listaInvitados = []

    def agregarInvitado():
        while True:
            nombre = input("Ingrese el nombre del invitado (o presione Enter para terminar): ")
            if nombre == "":
                break
            listaInvitados.append(nombre.capitalize())
            print(f"✅ {nombre.capitalize()} ha sido agregado a la lista.")

    def mostrarInvitados():
        if not listaInvitados:
            print("La lista de invitados está vacía.")
        else:
            print("\n📋 Lista de invitados:")
            for i, invitado in enumerate(listaInvitados):
                print(f"{i}: {invitado}")

    def mostrarUnInvitado():
        mostrarInvitados()
        if listaInvitados:
            try:
                indice = int(input("Ingrese el índice del invitado que desea mostrar: "))
                if 0 <= indice < len(listaInvitados):
                    print(f"👤 Invitado: {listaInvitados[indice]}")
                else:
                    print("❌ Índice inválido.")
            except ValueError:
                print("❌ Por favor, ingrese un número válido.")

    def eliminarInvitado():
        mostrarInvitados()
        if listaInvitados:
            try:
                indice = int(input("Ingrese el índice del invitado que desea eliminar: "))
                if 0 <= indice < len(listaInvitados):
                    eliminado = listaInvitados.pop(indice)
                    print(f"🗑️ {eliminado} ha sido eliminado de la lista.")
                else:
                    print("❌ Índice inválido.")
            except ValueError:
                print("❌ Por favor, ingrese un número válido.")

    def buscarInvitado():
        nombre = input("Ingrese el nombre del invitado a buscar: ").capitalize()
        resultados = [i for i, inv in enumerate(listaInvitados) if nombre.lower() in inv.lower()]
        if resultados:
            print(f"🔍 Resultados de la búsqueda para '{nombre}':")
            for i in resultados:
                print(f"{i}: {listaInvitados[i]}")
        else:
            print(f"❌ No se encontraron invitados que coincidan con '{nombre}'.")

    def modificarInvitado():
        mostrarInvitados()
        if listaInvitados:
            try:
                indice = int(input("Ingrese el índice del invitado que desea modificar: "))
                if 0 <= indice < len(listaInvitados):
                    nuevoNombre = input("Ingrese el nuevo nombre del invitado: ").capitalize()
                    listaInvitados[indice] = nuevoNombre
                    print(f"✏️ El nombre ha sido actualizado a {nuevoNombre}.")
                else:
                    print("❌ Indice inválido.")
            except ValueError:
                print("❌ Por favor, ingrese un número válido.")

    def mostrarMenu():
        print("\n🎉 BIENVENIDO A LA GESTIÓN DE INVITADOS PARA LA FIESTA 🎉")
        print("1. Agregar invitado")
        print("2. Mostrar un invitado")
        print("3. Eliminar invitado")
        print("4. Buscar un invitado")
        print("5. Modificar invitado")
        print("6. Mostrar lista completa")
        print("7. Salir")

    def menu():
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
            elif opcion == "7":
                print("\n👋 ¡Gracias por usar el programa!\n")
                break
            else:
                print("\n❌ Opción no válida. Por favor, seleccione una opción del 1 al 7.\n")

    menu()

invitadosApp()
