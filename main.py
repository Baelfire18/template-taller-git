import random  # importamos libreria random casos 'aleatoreos'
import os  # importamos libreria para interactuar con archivos

print(
    """
  ____    _                                         _       _                         
 | __ )  (_)   ___   _ __   __   __   ___   _ __   (_)   __| |   ___    ___      __ _ 
 |  _ \  | |  / _ \ | '_ \  \ \ / /  / _ \ | '_ \  | |  / _` |  / _ \  / __|    / _` |
 | |_) | | | |  __/ | | | |  \ V /  |  __/ | | | | | | | (_| | | (_) | \__ \   | (_| |
 |____/  |_|  \___| |_| |_|   \_/    \___| |_| |_| |_|  \__,_|  \___/  |___/    \__,_|
  ____     ____    ____                  _                             _   _                 
 |  _ \   / ___|  / ___|   __ _    ___  | |__     ___    _ __   _ __  (_) | |_    ___    ___ 
 | | | | | |     | |      / _` |  / __| | '_ \   / _ \  | '__| | '__| | | | __|  / _ \  / __|
 | |_| | | |___  | |___  | (_| | | (__  | | | | | (_) | | |    | |    | | | |_  | (_) | \__ \\
 |____/   \____|  \____|  \__,_|  \___| |_| |_|  \___/  |_|    |_|    |_|  \__|  \___/  |___/


^..^      /     ^..^      /     ^..^      /     ^..^      /     ^..^      /     ^..^      /
/_/\_____/      /_/\_____/      /_/\_____/      /_/\_____/      /_/\_____/      /_/\_____/
   /\   /\\         /\   /\\         /\   /\\         /\   /\\         /\   /\\         /\   /\\
  /  \ /  \\       /  \ /  \\       /  \ /  \\       /  \ /  \\       /  \ /  \\       /  \ /  \\

"""
)

# Usamos la libreria os para obtener la lista de archivos dentro de la carpeta fotos
lista_de_fotos = os.listdir("fotos")

# Imprimimos los archivos de fotos disponibles
print("Opciones disponibles:")
print(lista_de_fotos, "\n")

input("Presiona ENTER para obtener una foto al azar de perritos ")

# Usamos la funcion choice de random para obtener una foto al azar
foto_aleatorea = random.choice(lista_de_fotos)

# Concatenamos para obtener la ruta completa de la foto
ruta_foto = f"fotos\\{foto_aleatorea}"

# Usamos la liberia os para abrir la foto seleccionada
os.startfile(ruta_foto)

print(
    """
  ____            _               _               
 / ___|    __ _  | |  _   _    __| |   ___    ___ 
 \___ \   / _` | | | | | | |  / _` |  / _ \  / __|
  ___) | | (_| | | | | |_| | | (_| | | (_) | \__ \\
 |____/   \__,_| |_|  \__,_|  \__,_|  \___/  |___/
"""
)
