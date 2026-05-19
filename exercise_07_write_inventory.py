# Ejercicio 7 - Escribir un inventario ordenado


def write_inventory(filename, inventory):
    """
    Escribe el inventario en un archivo, una línea por item, ordenadas
    alfabéticamente por nombre de item, con el formato:

        item:cantidad

    Reglas:
    - Cada línea debe terminar con "\\n".
    - Si el diccionario está vacío, el archivo se crea vacío.
    - Si el archivo ya existía, se sobreescribe.
    - La función no retorna nada (None).

    Args:
        filename: str - nombre del archivo a escribir.
        inventory: dict[str, int] - item -> cantidad.

    Returns:
        None

    Ejemplo:
        write_inventory("stock.txt", {"wood": 10, "coal": 3, "iron": 7})
        # El archivo stock.txt queda con:
        # coal:3
        # iron:7
        # wood:10
    """
    with open (filename, "w") as archivo:
        lista = [""]
        for clave, valor in inventory.items():
            if lista == [""]:
                lista.append(clave)
            else:
                for i in range(len(lista)):
                    if lista[i] > clave:
                        lista.insert(i, clave)
        for k in range (len(lista)):
            for key, value in inventory.items():
                if lista[k] == key:
                    archivo.write(f"{key}:{value}\n")
