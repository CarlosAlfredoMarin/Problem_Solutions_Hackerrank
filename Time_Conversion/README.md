Leemos la hora ingresada por teclado y lo guardamos como un ```str```
```python
string: str = read_Prhase()
```
```python
def read_Prhase() -> str:
    phrase: str = input()
    return phrase
```

Convertimos ese ```str``` en una ```lista```
```python
list_string: list[str] = Convert_Str_to_List(string) 
```
```python
def Convert_Str_to_List(string: str) -> list[str]:
    list1 = []
    list1[:0] = string
    return list1
```

Separamos los elementos de Hora, Minutos y Segundos
```python
Militar: list[str] = Time_Conversion(list_string)
```
```python
def Time_Conversion(list1: list[str]) ->list[str]:
    HH: int = int(list1[0] + list1[1])
    MM: int = int(list1[3] + list1[4])
    SS: int = int(list1[6] + list1[7])
```
Validamos si la hora ingresada fue ```AM``` o ```PM```
```python
    if list1[len(list1)-2] == "A":
        if list1[0] == '1':
            list1[0] = '0'
            list1[1] = '0'
    elif list1[len(list1)-2] == "P" and list1[0] == '1' and list1[1] != '1':
        pass
    elif list1[len(list1)-2] == "P":
        HH = 12 + HH
        Aux : list[str] = Convert_Int_to_Str(HH)
        list1[0] = Aux[0]
        list1[1] = Aux[1]
    return list1
```

Convertimos la lista en un ```str``` para poder mostrarlo en consola
```python
Convert_List_to_Str(Militar)
```
```python
def Convert_List_to_Str(list1: list[str]) -> str:
    list1.pop(9)
    list1.pop(8)
    String: str = "".join([str(_) for _ in list1])
    print(String)
    return String
```
