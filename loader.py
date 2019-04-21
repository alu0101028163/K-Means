import sys              # Command line arguments
import re               # Regular expressions
import numpy as np      # Arrays for high performance operations

''' Esta función carga un fichero del directorio principal
y obtiene de este el número de entradas, su dimensión, y por supuesto
las entradas en sí
'''
def load(*args, **kwds):
    file = ""
    # Puede ser llamado un fichero por argumentos o de manera explícita.
    if len(args) == 0:
        file = sys.argv[2]
    elif len(args) == 1 and isinstance(args[0], str):
        file = args[0]
    f = open(file, "r")
    number_of_entries = f.readline()
    dimension = f.readline()
    entries = []

    # Se utilizan expresiones regulares para limpiar la entrada en caso
    # de que contenga ciertos caracteres que pueden corromper la lectura,
    # como comas en lugar de puntos para los números flotantes o tabuladores
    # en lugar de espacios simples.
    for line in f:
        line = re.sub(r'[,]', r'.', line) # Changes commas for dots
        line = re.sub(r'\t', r' ', line)  # Changes tabs for spaces
        line = line.split(' ')            # Breaks the line by its spaces and returns a list.
        points = [float(point) for point in line]
        entries.append(points)
    f.close()

    entries = np.array(entries)
    return entries, int(dimension), int(number_of_entries)
