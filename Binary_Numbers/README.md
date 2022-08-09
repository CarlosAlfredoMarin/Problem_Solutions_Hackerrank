Creamos una lista vacía
```python 
one_list: list[int] = []
```

Leemos el número entero ingresado
```python 
n = int(input().strip())
```

Dividimos el número entre 2 todas las veces que sea posible
```python
one_list: list[int] = DecimalToBinary(n)
```
```python
def DecimalToBinary(num) -> list[int]:
    if num >= 1:
        DecimalToBinary(num // 2)
    one_list.append(num % 2)
    return(one_list) 
```

Creamos algunas variables que usaremos más adelante
```python
count: int = 0
count2: int = 0
 m: int = 0
 ```

Recorremos toda la lista
```python
while (m<len(one_list)):
    (count2, m) = CountOnes2(one_list, m)
    if count2>count:
        count = count2
print(count)
 ```

Contamos los  ```1``` consecutivos
```python
def CountOnes2(one_list: list[int], m:int):
    count: int = 0
    n: int = len(one_list)
    Aux: int = 0

    for i in range(m,n):
        if (one_list[i] == 1):
            count += 1
            if i==n-1:
                Aux = i+1
        elif (one_list[i] == 0):
            Aux = i+1
            break
        
    return (count, Aux)
```
