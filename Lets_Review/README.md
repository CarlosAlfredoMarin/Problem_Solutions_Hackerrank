Leemos el entero ingresado por consola
```python 
N = int(input())
```

Leemos las palabras ingresadas por teclado
```python 
words = fill_list()
```
```python 
def fill_list() -> list[str]:
    words: list[str] = []
    words = [input() for i in range(0,N)]
    return words
```

Separamos cada una de las letras y las guardamos en una lista
```python 
Letters: list[str] = [convert_word_to_str(words[i]) for i in range(0, N)]
```
```python 
def convert_word_to_str(string):
    list1=[]
    list1[:0]=string
    return list1
```

Vamos imprimiendo en consola las letras
```python 
for i in range(0, len(words)):
    even_indices(Letters[i])
    print(" ", end="")
    odd_indices(Letters[i])
    print(" ")
```

Creamos una nueva lista que contiene únicamente las letras de los índices pares
```python 
def even_indices(words: list[str]):
    even_letters: list[str] = [words[i] for i in range(0,len(words)) if i%2==0]
    StrA = "".join(even_letters)
    print(StrA, end="")
```

Creamos una nueva lista que contiene únicamente las letras de los índices impares
```python 
def odd_indices(words: list[str]):
    odd_letters: list[str] = [words[i] for i in range(0,len(words)) if i%2!=0]
    StrA = "".join(odd_letters)
    print(StrA, end="")
```
