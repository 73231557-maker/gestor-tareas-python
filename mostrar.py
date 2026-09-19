def mostrar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas pendientes.")
    else:
        print("Lista de Tareas pendientes:")
        for indice, tarea in enumerate(lista_tareas):
            print(f"{indice}. {tarea}")