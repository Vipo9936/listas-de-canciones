# Lista de canciones
canciones = [  # Se define una lista inicial de canciones
    {
        "nombre": "Lady (Hear Me Tonight)",
        "artista": "Modjo",
        "duracion": "3:41",
        "reproducciones": 549963023
    },
    {
        "nombre": "Alors on danse",
        "artista": "Stromae",
        "duracion": "3:54",
        "reproducciones": 425000
    },
    {
        "nombre": "Reencuentro",
        "artista": "DLD",
        "duracion": "5:47",
        "reproducciones": 300017160585
    },
    {
        "nombre": "Historia Sin Fin",
        "artista": "Banda Machos",
        "duracion": "3:04",
        "reproducciones": 124533711
    },
    {
        "nombre": "Alma Enamorada",
        "artista": "Chalino Sánchez",
        "duracion": "2:39",
        "reproducciones": 2053092389
    }
]

def artistas_unica_palabra(canciones):
    """Devuelve una lista de artistas que tienen solo una palabra en su nombre."""
    artistas_unica_palabra = []
    for cancion in canciones:
        artista = cancion["artista"]  # Obtiene el nombre del artista
        if len(artista.split()) == 1:  # Verifica si el artista tiene solo una palabra
            artistas_unica_palabra.append(artista)  # Agrega a la lista si es de una palabra
    return artistas_unica_palabra

def mostrar_canciones(canciones):
    """Muestra todas las canciones en la lista."""
    print("\nLista de Canciones:")
    for cancion in canciones:
        print(f"{cancion['nombre']} - {cancion['artista']} (Duración: {cancion['duracion']})")

def mostrar_artistas(canciones):
    """Muestra todos los artistas únicos en la lista de canciones."""
    artistas = set(cancion["artista"] for cancion in canciones)  # Crea un conjunto de artistas únicos
    print("\nLista de Artistas:")
    for artista in artistas:
        print(artista)  # Imprime cada artista

def agregar_cancion(canciones):
    """Permite al usuario agregar una nueva canción a la lista."""
    nombre = input("Ingrese el nombre de la canción: ")  # Pide el nombre de la canción
    artista = input("Ingrese el nombre del artista o banda: ")  # Pide el nombre del artista
    duracion = input("Ingrese la duración de la canción (formato mm:ss): ")  # Pide la duración
    
    # Validación de la duración
    while True:
        try:
            minutos, segundos = map(int, duracion.split(":"))
            if 0 <= minutos < 60 and 0 <= segundos < 60:
                break
            else:
                print("Duración inválida. Asegúrese de que los minutos y segundos estén entre 0 y 59.")
                duracion = input("Ingrese la duración de la canción (formato mm:ss): ")
        except ValueError:
            print("Formato inválido. Por favor, ingrese la duración en formato mm:ss.")
            duracion = input("Ingrese la duración de la canción (formato mm:ss): ")
    
    while True:
        try:
            reproducciones = int(input("Ingrese la cantidad de reproducciones: "))  # Pide las reproducciones
            if reproducciones < 0:
                print("La cantidad de reproducciones no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido para las reproducciones.")

    nueva_cancion = {  # Crea un diccionario para la nueva canción
        "nombre": nombre,
        "artista": artista,
        "duracion": duracion,
        "reproducciones": reproducciones
    }
    
    canciones.append(nueva_cancion)  # Agrega la nueva canción a la lista
    print("Canción agregada exitosamente.")  # Mensaje de confirmación

def main():
    while True:  # Bucle infinito para mostrar el menú
        print("\nMenú:")
        print("1. Mostrar artistas de una sola palabra")
        print("2. Mostrar todas las canciones")
        print("3. Mostrar todos los artistas")
        print("4. Agregar una nueva canción")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")  # Pide al usuario que seleccione una opción

        # Diccionario que simula un switch para ejecutar la opción seleccionada
        opciones = {
            "1": lambda: print("Artistas que solo tienen una palabra:", artistas_unica_palabra(canciones)),
            "2": lambda: mostrar_canciones(canciones),
            "3": lambda: mostrar_artistas(canciones),
            "4": lambda: agregar_cancion(canciones),
            "5": lambda: exit("Saliendo del programa...") 
        }

        # Ejecuta la opción seleccionada
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción no válida. Intente de nuevo.")  

# Aqui se ejecuta el programa
if __name__ == "__main__":
    main()
