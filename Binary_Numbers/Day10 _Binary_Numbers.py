one_list: list[int] = []

def DecimalToBinary(num) -> list[int]:
    if num >= 1:
        DecimalToBinary(num // 2)
    one_list.append(num % 2)
    return(one_list) 
             

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


if __name__ == '__main__':
    n = int(input().strip())
    one_list: list[int] = DecimalToBinary(n)

    count: int = 0
    count2: int = 0
    m: int = 0

    while (m<len(one_list)):
        (count2, m) = CountOnes2(one_list, m)
        if count2>count:
            count = count2
    print(count)