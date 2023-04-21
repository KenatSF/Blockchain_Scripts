





def findDuplicated(lista):
    base = set()
    for x in lista:
        if x in base:
            return x
        else:
            base.add(x)
    return None


def main():


    a_list = [7,1,1,7]

    answer = findDuplicated(a_list)
    print(answer)


if __name__ == "__main__":
    main()
