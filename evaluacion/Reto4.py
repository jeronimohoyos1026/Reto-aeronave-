aeronaves = []


def registrar_aeronave():
    print("\n--- Registro de aeronave ---")
    matricula = input("Ingrese la matrícula de la aeronave: ")
    modelo = input("Ingrese el modelo de la aeronave: ")
    horas_vuelo = float(input("Ingrese las horas de vuelo acumuladas: "))

    aeronave = {
        "matricula": matricula,
        "modelo": modelo,
        "horas_vuelo": horas_vuelo,
        "componentes": []
    }

    cantidad_componentes = int(input("¿Cuántos componentes críticos desea registrar? "))

    for i in range(cantidad_componentes):
        print(f"\nComponente {i + 1}")
        nombre = input("Nombre del componente: ")
        horas_uso = float(input("Horas de uso actuales: "))
        limite_horas = float(input("Límite máximo permitido antes del mantenimiento: "))

        componente = {
            "nombre": nombre,
            "horas_uso": horas_uso,
            "limite_horas": limite_horas
        }

        aeronave["componentes"].append(componente)

    aeronaves.append(aeronave)
    print(f"\nLa aeronave {matricula} fue registrada correctamente.")


def generar_reporte_mantenimiento():
    print("\n--- Reporte de mantenimiento ---")

    if len(aeronaves) < 3:
        print("Debe registrar al menos 3 aeronaves antes de consultar el reporte.")
        return []

    componentes_mantenimiento = []

    for aeronave in aeronaves:
        for componente in aeronave["componentes"]:
            if componente["horas_uso"] > componente["limite_horas"]:
                componentes_mantenimiento.append(componente)
                print(
                    f"Aeronave: {aeronave['matricula']} | "
                    f"Modelo: {aeronave['modelo']} | "
                    f"Componente: {componente['nombre']} | "
                    f"Horas de uso: {componente['horas_uso']} | "
                    f"Límite permitido: {componente['limite_horas']} | "
                    "Estado: REQUIERE CAMBIO"
                )

    if not componentes_mantenimiento:
        print("No se encontraron componentes que hayan superado el límite de horas.")
    return componentes_mantenimiento


def realizar_mantenimiento():
    componentes_mantenimiento = generar_reporte_mantenimiento()

    if not componentes_mantenimiento:
        return

    respuesta = input(
        "¿Desea realizar mantenimiento a los componentes reportados? (SI/NO): "
    )

    if respuesta == "NO":
        print(
            "Al avión no se le hizo mantenimiento. El reporte y las horas de uso "
            "y de vuelo se mantienen tal como están."
        )
        return
    if respuesta != "SI":
        print("Respuesta no válida. Las horas de uso se mantienen sin cambios.")
        return

    while True:
        matricula = input("Ingrese la placa de la aeronave: ")
        aeronave_encontrada = False

        for aeronave in aeronaves:
            if aeronave["matricula"] == matricula:
                aeronave_encontrada = True
                horas_vuelo = float(
                    input("Ingrese las horas de vuelo actuales de la aeronave: ")
                )
                aeronave["horas_vuelo"] = horas_vuelo
                for componente in aeronave["componentes"]:
                    if componente["horas_uso"] > componente["limite_horas"]:
                        print(
                            f"El componente {componente['nombre']} superó el límite "
                            "y se tendrá que cambiar."
                        )
                        componente["horas_uso"] = 0
                aeronave["horas_vuelo"] = 0
                print(
                    f"Mantenimiento realizado a la aeronave {matricula}. "
                    f"Sus {horas_vuelo} horas de vuelo vuelven a 0."
                )
                break

        if not aeronave_encontrada:
            print("No se encontró una aeronave con esa placa.")

        respuesta_otra = input(
            "¿Desea realizar mantenimiento a otra aeronave? (SI/NO): "
        )
        if respuesta_otra != "SI":
            break


while True:
    print("\n=== SISTEMA DE GESTIÓN DE AERONAVES ===")
    print("1. Registrar aeronave")
    print("2. Ver reporte de mantenimiento")
    print("3. Realizar mantenimiento")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_aeronave()
    elif opcion == "2":
        generar_reporte_mantenimiento()
    elif opcion == "3":
        realizar_mantenimiento()
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
