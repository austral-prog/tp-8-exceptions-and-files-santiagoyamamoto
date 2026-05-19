# Ejercicio 6 - Estadísticas de notas por estudiante


def grades_stats(filename):
    """
    Lee un archivo donde cada línea tiene el formato:

        estudiante:nota1,nota2,nota3,...

    y retorna un diccionario donde la clave es el nombre del estudiante y
    el valor es una TUPLA (promedio, maximo, minimo) con los tres valores
    como float.

    Reglas:
    - El promedio se calcula con todas las notas de la línea.
    - Las líneas vacías se ignoran.
    - Se garantiza que todas las notas son números válidos.
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, tuple[float, float, float]] - estadísticas por estudiante.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "Ana:8,9,7\nBeto:5,5,10\nCami:10\n"
        grades_stats("notas.txt") -> {
            "Ana": (8.0, 9.0, 7.0),
            "Beto": (6.666666666666667, 10.0, 5.0),
            "Cami": (10.0, 10.0, 10.0),
        }
    """

    with open (filename, "r") as archivo:
        dic = {}
        for linea in archivo:
            if linea.strip() == "":
                pass
            else:
                lista = []
                total = 0
                cant = 0
                maximo = 0
                minimo = 0
                sep = linea.split(":")
                sup = sep[1].split(",")
                for i in sup:
                    total += float(i)
                    cant += 1
                    if float(i) > maximo:
                        maximo = float(i)
                    if minimo == 0:
                        minimo = float(i)
                    else:
                        if minimo > float(i):
                            minimo = float(i)
                lista.append(total / cant)
                lista.append(maximo)
                lista.append(minimo)
                dic[sep[0]] = tuple(lista)
        return dic


