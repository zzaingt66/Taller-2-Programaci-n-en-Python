def Agenda():   
    # Inicializa un diccionario vacío para almacenar los contactos.
    agenda = {}

    def addContact():
        # Esta función agrega nuevos contactos a la agenda.
        while True:
            nombre = input("Ingrese el nombre del contacto: ").capitalize()
            # Solicita al usuario el nombre del contacto y lo capitaliza.
            if nombre == "":
                # Si el nombre está vacío, termina el bucle.
                break
            telefono = input("Ingrese el número de teléfono: ")
            # Solicita al usuario el número de teléfono del contacto.
            agenda[nombre] = {
                "telefono": telefono
            }
            # Añade el contacto a la agenda con su número de teléfono.
            print(f"\n✅ Contacto '{nombre}' agregado exitosamente.\n")
            # Imprime un mensaje de confirmación.

    def showContact():
        # Esta función muestra la información de un contacto específico.
        if agenda:
            # Verifica si la agenda no está vacía.
            print("\n📒 AGENDA DE CONTACTOS:")
            # Muestra la lista de contactos.
            showAgenda()
            # Solicita al usuario seleccionar un índice de contacto.
            indice = int(input("\nSeleccione el índice del contacto que desea ver: ")) - 1
            # Convierte la entrada del usuario en un índice válido (0 basado).
            if 0 <= indice < len(agenda):
                # Verifica si el índice está dentro del rango válido.
                nombre = list(agenda.keys())[indice]
                # Obtiene el nombre del contacto basado en el índice.
                contacto = agenda[nombre]
                # Obtiene los detalles del contacto.
                print(f"\n🔎 Información del Contacto:")
                print(f"Nombre: {nombre}")
                print(f"Teléfono: {contacto['telefono']}\n")
                # Muestra la información del contacto.
            else:
                print("\n❌ Índice no válido.\n")
                # Mensaje de error si el índice no es válido.
        else:
            print("\n⚠️ La agenda está vacía.\n")
            # Mensaje si la agenda está vacía.

    def modifyContact():
        # Esta función permite modificar un contacto existente.
        if agenda:
            print("\n📒 AGENDA DE CONTACTOS:")
            showAgenda()
            # Muestra la lista de contactos.
            indice = int(input("\nSeleccione el índice del contacto a modificar: ")) - 1
            # Solicita al usuario seleccionar un índice de contacto.
            if 0 <= indice < len(agenda):
                nombre = list(agenda.keys())[indice]
                # Obtiene el nombre del contacto basado en el índice.
                print(f"\n✏️ Modificando el contacto '{nombre}':")
                print("Ingrese los nuevos datos (deje en blanco para mantener el valor actual):")
                nuevo_telefono = input("Nuevo teléfono: ")
                # Solicita el nuevo número de teléfono del contacto.
                
                if nuevo_telefono:
                    agenda[nombre]["telefono"] = nuevo_telefono
                    # Actualiza el número de teléfono si se ingresa uno nuevo.
                print("\n✅ Contacto modificado exitosamente.\n")
                # Imprime un mensaje de confirmación.
            else:
                print("\n❌ Índice no válido.\n")
                # Mensaje de error si el índice no es válido.
        else:
            print("\n⚠️ La agenda está vacía.\n")
            # Mensaje si la agenda está vacía.

    def deleteContact():
        # Esta función elimina un contacto de la agenda.
        if agenda:
            print("\n📒 AGENDA DE CONTACTOS:")
            showAgenda()
            # Muestra la lista de contactos.
            indice = int(input("\nSeleccione el índice del contacto a eliminar: ")) - 1
            # Solicita al usuario seleccionar un índice de contacto.
            if 0 <= indice < len(agenda):
                nombre = list(agenda.keys())[indice]
                # Obtiene el nombre del contacto basado en el índice.
                del agenda[nombre]
                # Elimina el contacto de la agenda.
                print(f"\n✅ Contacto '{nombre}' eliminado exitosamente.\n")
                # Imprime un mensaje de confirmación.
            else:
                print("\n❌ Índice no válido.\n")
                # Mensaje de error si el índice no es válido.
        else:
            print("\n⚠️ La agenda está vacía.\n")
            # Mensaje si la agenda está vacía.

    def showAgenda():
        # Esta función muestra todos los contactos en la agenda.
        for i, (nombre, datos) in enumerate(agenda.items(), start=1):
            # Recorre los contactos en la agenda y muestra el índice, nombre y teléfono.
            print(f"{i}. {nombre} - Teléfono: {datos['telefono']}")
        print("-" * 30)
        # Imprime una línea separadora para mejorar la legibilidad.

    def searchContact():
        # Esta función busca un contacto específico por nombre.
        nombre = input("Ingrese el nombre del contacto que desea buscar: ").capitalize()
        # Solicita al usuario el nombre del contacto a buscar.
        if nombre in agenda:
            # Verifica si el nombre está en la agenda.
            print(f"\n🔎 Información del Contacto:")
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {agenda[nombre]['telefono']}\n")
            # Muestra la información del contacto si se encuentra.
        else:
            print("\n❌ El contacto no existe en la agenda.\n")
            # Mensaje de error si el contacto no se encuentra en la agenda.

    def mostrarMenu():
        # Esta función muestra el menú principal.
        print("\n📱 BIENVENIDO A SU AGENDA DE CONTACTOS 📱")
        print("1. Agregar contacto")
        print("2. Mostrar un contacto")
        print("3. Eliminar contacto")
        print("4. Buscar un contacto")
        print("5. Modificar contacto")
        print("6. Mostrar agenda completa")
        print("7. Salir")

    def menu():
        # Esta función maneja la selección de opciones del menú.
        opciones = {
            "1": addContact,
            "2": showContact,
            "3": deleteContact,
            "4": searchContact,
            "5": modifyContact,
            "6": showAgenda
        }
        while True:
            mostrarMenu()
            # Muestra el menú principal.
            opcion = input("Seleccione una opción: ")
            # Solicita al usuario seleccionar una opción del menú.
            if opcion in opciones:
                opciones[opcion]()
                # Llama a la función correspondiente según la opción seleccionada.
            elif opcion == "7":
                print("\n👋 ¡Hasta luego!\n")
                break
                # Sale del bucle y termina el programa si se selecciona la opción de salir.
            else:
                print("\n❌ Opción no válida. Por favor, seleccione una opción del 1 al 7.\n")
                # Mensaje de error si la opción seleccionada no es válida.

    menu()
    # Llama a la función menu() para iniciar la aplicación.

Agenda()
# Llama a la función Agenda() para ejecutar el programa.
