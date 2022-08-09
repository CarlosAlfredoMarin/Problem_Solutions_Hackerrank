Creamos una lista vacía
```python
lista = []
```

```python
Leemos la cantidad de números que van a ser ingresados
n = (int(input()))
```

Leemos los números ingresados uno a uno
```python
for i in range(0, n):
        lista.append(int(input()))
```

Ordenamos la lista
```python
lista_ordenada = ordenamiento_de_burbuja(lista)
```
```python
def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista
```

Mostramos los números ordenados uno a uno en consola
```python
for element in lista_ordenada:
        print(element)
```     
