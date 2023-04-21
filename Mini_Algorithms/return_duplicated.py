


def findDuplicated(lista):
    base = set()
    duplicated = set()
    for x in lista:
        if x in base:
            duplicated.add(x)
        else:
            base.add(x)
    return duplicated


def main():


    a_list = [7,1,1,7] 

    answer = findDuplicated(a_list)
    print(answer)


if __name__ == "__main__":
    main()
