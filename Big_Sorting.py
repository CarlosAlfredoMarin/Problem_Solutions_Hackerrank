def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


if __name__ == "__main__":
    
    lista = []

    n = (int(input()))

    for i in range(0, n):
        lista.append(int(input()))

    lista_ordenada = ordenamiento_de_burbuja(lista)
    for element in lista_ordenada:
        print(element)