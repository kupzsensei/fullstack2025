score = int(input("Score: "))

# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >=80 and score < 90:
#     print("Grade: B")
# elif score >=70 and score < 80:
#     print("Grade: C")
# elif score >=60 and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")


if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    return False
    # return True if n % 2 == 0 else False


main()