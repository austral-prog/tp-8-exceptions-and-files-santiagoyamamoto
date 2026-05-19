# Ejercicio 1 - Leer líneas de un archivo


def read_lines(filename):
    """
    Lee un archivo de texto y retorna una lista con sus líneas.

    Reglas:
    - Cada línea debe venir sin el salto de línea final y sin espacios
      al principio o al final (strip).
    - Las líneas vacías (o con solo espacios) se ignoran.
    - Si el archivo no existe, se debe propagar FileNotFoundError.
    - Si el archivo está vacío, retornar [].

    Args:
        filename: str - nombre (o ruta) del archivo a leer.

    Returns:
        list[str] - lista de líneas no vacías, en el orden del archivo.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "manzana\n  banana\npera\n"
        read_lines("datos.txt") -> ["manzana", "banana", "pera"]
    """

    with open(filename, "r") as archivo:
        lista = []
        for linea in archivo:
            limpia = linea.strip()
            if limpia != "":
                lista.append(limpia)
    return lista
