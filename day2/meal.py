def main():
    convert(input("what time is it ? : "))


def convert(time):
    hours , minutes = time.split(":")
    print(hours , "hours")
    print(minutes , "minutes")

    if int(hours) == 7 and int(minutes) < 60:
        print("breakfast time")
    elif int(hours) == 8 and int(minutes) == 0:
        print("breakfast time")


if __name__ == "__main__":
    main()