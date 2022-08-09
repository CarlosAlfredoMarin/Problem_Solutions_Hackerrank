def crear_listas() -> dict[str, str]:

    my_dict_0_19: dict[str, str] = {
        "0": "zero",
        "1": "one",
        "2": "two",     
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",    
        "10": "ten",
        "11": "eleven",  
        "12": "twelve", 
        "13": "thirteen",
        "14": "fourteen",
        "15": "fifteen",
        "16": "sixteen",
        "17": "seventeen",
        "18": "eighteen",
        "19": "nineteen",                                            
    }

    my_dict_decades: dict[str, str] = {
        "20": "twenty",
        "30": "thirty",
        "40": "fourty",
        "50": "fifty",
    }

    return lista_completa(my_dict_decades, my_dict_0_19)




def lista_completa(my_dict_decades, my_dict_0_19) -> dict[str, str]:    
    dict_0_60: dict[str, str] = {}
    dict_0_60 = dict(dict_0_60, **my_dict_0_19)
    dict_0_60 = dict(dict_0_60, **{"20": "twenty"})

    for j in range(2,6):
        dict_10s = {str(j)+str(i) : my_dict_decades[str(j*10)]+" "+my_dict_0_19[str(i)] for i in range(1,10)}
        dict_0_60 = dict(dict_0_60, **dict_10s)

        if j == 2:
            dict_0_60 = dict(dict_0_60, **{"30": "thirty"})
        elif j == 3:
            dict_0_60 = dict(dict_0_60, **{"40": "fourty"})
        elif j == 4:
            dict_0_60 = dict(dict_0_60, **{"50": "fifty"})
        elif j == 5:
            dict_0_60 = dict(dict_0_60, **{"60": "o\' clock"})        
        else:
            pass

    return dict_0_60




def timeInWords(h: int, m: int) -> str:
    dict = crear_listas()

    hour: str = dict[str(h)]
    minute: str = dict[str(m)]
    next_hour: str = dict[str(h+1)]
    rest: str = dict[str(60-m)]

    if m == 0:
        print(f'{hour} o\' clock')
    elif m == 1:
        print(f'{minute} minute past {hour}')
    elif m == 15:
        print(f'quarter past {hour}')
    elif m == 45:
        print(f'quarter to {next_hour}')
    elif m < 30:
        print(f'{minute} minutes past {hour}')
    elif m > 30:
        print(f'{rest} minutes to {next_hour}')
    elif m == 30:
        print(f'half past {hour}')
    


if __name__ == '__main__':
    h: int = int(input())
    m: int = int(input())
    timeInWords(h=h, m=m)