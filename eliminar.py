# eliminar.py

def eliminar_tarea(lista_tareas, indice):
    """
    Elimina una tarea de la lista basándose en su índice.
    """
    # Verificamos si el índice está dentro del rango válido de la lista
    if 0 <= indice < len(lista_tareas):
        # Usamos pop para eliminar el elemento en el índice indicado
        tarea_eliminada = lista_tareas.pop(indice)
        print(f"Tarea eliminada: {tarea_eliminada}")
        return lista_tareas
    else:
        # Condicional opcional si el índice no existe
        print("Error: El índice proporcionado no existe en la lista.")
        return lista_tareas

# --- Bloque de prueba (opcional, para verificar que funciona) ---
if __name__ == "__main__":
    mis_tareas = ["Estudiar", "Hacer ejercicio", "Comprar pan"]
    print("Lista original:", mis_tareas)
    
    # Intentamos borrar la tarea en el índice 1 ("Hacer ejercicio")
    mis_tareas = eliminar_tarea(mis_tareas, 1)
    print("Lista después de borrar:", mis_tareas)