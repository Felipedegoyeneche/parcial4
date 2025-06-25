def validar_codigo(codigo):
    tiene_mayus = any(c.isupper() for c in codigo)
    tiene_num = any(c.isdigit() for c in codigo)
    sin_espacios = " " not in codigo
    largo_ok = len(codigo) >= 6
    return tiene_mayus and tiene_num and sin_espacios and largo_ok

def comprar_entrada(entradas):
    nombre = input("Ingrese nombre de comprador: ").strip()
    if nombre in entradas:
        print("El nombre ya fue registrado.")
        return

    tipo = input("Ingrese tipo de entrada (G/V): ").strip().upper()
    if tipo not in ["G", "V"]:
        print("Tipo de entrada inválido. Solo se permite 'G' o 'V'.")
        return

    while True:
        codigo = input("Ingrese código de confirmación: ").strip()
        if validar_codigo(codigo):
            print("Código validado. ¡Entrada registrada con éxito!")
            entradas[nombre] = {"tipo": tipo, "codigo": codigo}
            break
        else:
            print("Código no válido. Intente otra vez.")

def consultar_comprador(entradas):
    nombre = input("Ingrese nombre de comprador a buscar: ").strip()
    if nombre in entradas:
        info = entradas[nombre]
        print(f"Tipo de entrada: {info['tipo']}, Código: {info['codigo']}")
    else:
        print("El comprador no se encuentra.")

def cancelar_compra(entradas):
    nombre = input("Ingrese nombre de comprador a cancelar: ").strip()
    if nombre in entradas:
        del entradas[nombre]
        print("¡Compra cancelada!")
    else:
        print("No se pudo cancelar la compra.")

def mostrar_menu():
    print("\nMENU PRINCIPAL")
    print("1.- Comprar entrada.")
    print("2.- Consultar comprador.")
    print("3.- Cancelar compra.")
    print("4.- Salir.")


if __name__ == "__main__":
    main()
