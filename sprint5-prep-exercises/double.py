def double(value):
    return value * 2


def double2(number):
    return number * 3


def main():
    # "22" is a string --> it will return string: "2222"
    print(double("22"))
    # in this function that expected to double the number, it multiplied by 3 ( probably accidental mistype)
    print(double2(10))  # return 30 instead of 20


if __name__ == "__main__":
    main()
