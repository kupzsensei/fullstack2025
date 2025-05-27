
def main():
    x = int_input("give me an X : ")
    y = int_input("give me an Y : ")

    print(x * y)


def int_input(label):
    x = input(label)
    # print(x.isnumeric())

    if x.isnumeric():
        return int(x)
    else:
        return 0


main()
