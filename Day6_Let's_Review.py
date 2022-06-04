def fill_list() -> list[str]:
    words: list[str] = []
    words = [input() for i in range(0,N)]
    return words


def convert_word_to_str(string):
    list1=[]
    list1[:0]=string
    return list1


def even_indices(words: list[str]):
    even_letters: list[str] = [words[i] for i in range(0,len(words)) if i%2==0]
    StrA = "".join(even_letters)
    print(StrA, end="")


def odd_indices(words: list[str]):
    odd_letters: list[str] = [words[i] for i in range(0,len(words)) if i%2!=0]
    StrA = "".join(odd_letters)
    print(StrA, end="")
    

if __name__ == '__main__':
    N = int(input())
    words = fill_list()
    Letters: list[str] = [convert_word_to_str(words[i]) for i in range(0, N)]

    for i in range(0, len(words)):
        even_indices(Letters[i])
        print(" ", end="")
        odd_indices(Letters[i])
        print(" ")