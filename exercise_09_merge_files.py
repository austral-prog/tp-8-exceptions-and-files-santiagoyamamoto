# Ejercicio 9 - Combinar dos archivos


def merge_files(file1, file2, output):
    """
    Lee file1 y file2 y escribe su concatenación (primero file1, luego
    file2) en el archivo output.

    Reglas:
    - Si file1 o file2 no existen, NO se debe crear el archivo de salida
      y se debe propagar FileNotFoundError. Esto implica que tenés que
      leer AMBOS archivos antes de empezar a escribir el output (si
      abrís output primero se crea aunque haya error después).
    - Si output ya existe, se sobreescribe.
    - La función no retorna nada (None).

    Args:
        file1: str - primer archivo a leer.
        file2: str - segundo archivo a leer.
        output: str - archivo de salida donde se escribe la concatenación.

    Returns:
        None

    Raises:
        FileNotFoundError: si file1 o file2 no existen.

    Ejemplo:
        # a.txt contiene "hola\n", b.txt contiene "mundo\n"
        merge_files("a.txt", "b.txt", "out.txt")
        # out.txt queda con:
        # hola
        # mundo
    """

    with open (file1, "r") as archivo:
        contenido = archivo.read()

    with open (file2, "r") as archivo2:
        contenido2 = archivo2.read()

    with open (output, "w") as final:
        final.write(contenido + contenido2)
