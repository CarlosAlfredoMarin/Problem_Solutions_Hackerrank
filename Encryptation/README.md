Primero leemos la frase ingresada desde el teclado, la almacenamos en una variable de tipo ```str```
```python
phrase: str = readPrhase()
```
```python
def readPrhase() -> str:
    phrase: str = input()
    return phrase
```

Removemos todos los espacios
```python
string: str = removeSpaces(phrase)
```
```python
def removeSpaces(phrase) -> str:
    s: str = phrase.replace(" ", "")
    return s
```

Convertimos el la variable de tipo ```str``` en una ```lista ```
```python
list_string: list[str] = convert_str_to_list(string) 
```
```python
def convert_str_to_list(string: str) -> list[str]:
    list1 = []
    list1[:0] = string
    return list1
```

Contamos la cantidad de letras que tiene la lista
```python
L: int = len(list_string)
```

Sacamos la raíz cuadrada a ese número
```python
root: float = math.sqrt(L)
```

Con la función ```piso``` y ```techo``` obtenemos el número de filas y columnas que usaremos
```python
rows: int = math.floor(root)
columns: int = math.ceil(root)
```

Nos aseguramos que se cumpla la condición $filas*columnas \geq L $
```python
if rows * columns < L:
        rows += 1
```

Creamos una ```lista anidada```, es decir, una lista de listas
```python
nested_list: list[str] = nested_list(rows, columns, list_string)
```
```python
def nested_list(rows:int, columns:int, list_string: list[str]) -> list[str]:
    list1: list[str] = [list_string[columns*i:columns*(i+1)] for i in range(0,rows)]
    return list1
```

Detectamos cuántos espacios quedaron vacíos, sin ninguna letra
```python
spaces_to_fill: int = spaces_to_fill(rows, nested_list)
```
```python
def spaces_to_fill(rows:int, list1: list[str]) -> list[str]:
    complete_list: list[str] = []
    spaces_to_fill: int = 0
    spaces_to_fill = len(list1[rows-2]) - len(list1[rows-1])
    return spaces_to_fill
```

Llenamos los espacios que no contienen ninguna letra con un elemento ```espacio```  de tipo ```str``` 
```python
complete_list: list[str] = fill_spaces(rows, spaces_to_fill, nested_list)
```
```python
def fill_spaces(rows:int, spaces_to_fill: int, list1: list[str]) -> list[str]:
    complete_list = list1
    for i in range(0, spaces_to_fill): complete_list[rows-1].append(" ")
    return complete_list
```

Organizamos las palabras de forma que se puedan mostrar en una única línea de la consola
```python
organize_words(rows, columns, complete_list)
```
```python
def organize_words(rows:int, columns:int, complete_list:list[str]):
    for j in range(0, columns):
        encrypted_list: list[str] = column_list(rows, j, complete_list) 
        list_str_1: list[str] = convert_to_list_str_1(encrypted_list)
        print(removeSpaces(list_str_1), end=" ")
```

Para ello, es necesario tomar cada columna de la matriz que construimos, y crear una nueva lista con esos elementos
```python
def column_list(rows:int, j:int, list1: list[str]) -> list[str]:
    column_list: list[str] = []
    column_list = [list1[i][j] for i in range(0,rows)]
    return column_list
```

Es necesario convertir las lista en ```str``` para poder mostrarlo en consola
```python
def convert_to_list_str_1(list1: list[str]) -> list[str]:
    list_str_1: list[str] = "".join(list1)
    return list_str_1
```
