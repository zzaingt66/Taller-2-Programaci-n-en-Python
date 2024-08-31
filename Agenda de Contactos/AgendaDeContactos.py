def Agenda():   
    agenda = {}

    def addContact():
        while True:
            nombre = input("Ingrese el nombre del contacto: ").capitalize()
            if nombre == "":
                break
            telefono = input("Ingrese el número de teléfono: ")
            agenda[nombre] = {
                "telefono": telefono
            }
            print(f"\n✅ Contacto '{nombre}' agregado exitosamente.\n")
            

    def showContact():
        if agenda:
            print("\n📒 AGENDA DE CONTACTOS:")
            showAgenda()
            indice = int(input("\nSeleccione el índice del contacto que desea ver: ")) - 1
            if 0 <= indice < len(agenda):
                nombre = list(agenda.keys())[indice]
                contacto = agenda[nombre]
                print(f"\n🔎 Información del Contacto:")
                print(f"Nombre: {nombre}")
                print(f"Teléfono: {contacto['telefono']}\n")
            else:
                print("\n❌ Índice no válido.\n")
        else:
            print("\n⚠️ La agenda está vacía.\n")

    def modifyContact():
        if agenda:
            print("\n📒 AGENDA DE CONTACTOS:")
            showAgenda()
            indice = int(input("\nSeleccione el índice del contacto a modificar: ")) - 1
            if 0 <= indice < len(agenda):
                nombre = list(agenda.keys())[indice]
                print(f"\n✏️ Modificando el contacto '{nombre}':")
                print("Ingrese los nuevos datos (deje en blanco para mantener el valor actual):")
                nuevo_telefono = input("Nuevo teléfono: ")
                
                if nuevo_telefono:
                    agenda[nombre]["telefono"] = nuevo_telefono
                print("\n✅ Contacto modificado exitosamente.\n")
            else:
                print("\n❌ Índice no válido.\n")
        else:
            print("\n⚠️ La agenda está vacía.\n")

    def deleteContact():
        if agenda:
            print("\n📒 AGENDA DE CONTACTOS:")
            showAgenda()
            indice = int(input("\nSeleccione el índice del contacto a eliminar: ")) - 1
            if 0 <= indice < len(agenda):
                nombre = list(agenda.keys())[indice]
                del agenda[nombre]
                print(f"\n✅ Contacto '{nombre}' eliminado exitosamente.\n")
            else:
                print("\n❌ Índice no válido.\n")
        else:
            print("\n⚠️ La agenda está vacía.\n")

    def showAgenda():
        for i, (nombre, datos) in enumerate(agenda.items(), start=1):
            print(f"{i}. {nombre} - Teléfono: {datos['telefono']}")
        print("-" * 30)

    def searchContact():
        nombre = input("Ingrese el nombre del contacto que desea buscar: ").capitalize()
        if nombre in agenda:
            print(f"\n🔎 Información del Contacto:")
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {agenda[nombre]['telefono']}\n")
        else:
            print("\n❌ El contacto no existe en la agenda.\n")

    def mostrarMenu():
        print("\n📱 BIENVENIDO A SU AGENDA DE CONTACTOS 📱")
        print("1. Agregar contacto")
        print("2. Mostrar un contacto")
        print("3. Eliminar contacto")
        print("4. Buscar un contacto")
        print("5. Modificar contacto")
        print("6. Mostrar agenda completa")
        print("7. Salir")

    def menu():
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
            opcion = input("Seleccione una opción: ")
            if opcion in opciones:
                opciones[opcion]()
            elif opcion == "7":
                print("\n👋 ¡Hasta luego!\n")
                break
            else:
                print("\n❌ Opción no válida. Por favor, seleccione una opción del 1 al 7.\n")

    menu()

Agenda()
