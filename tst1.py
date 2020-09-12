
def main():
    print("input two numbers")
    num1 = int(input())
    num2 = int(input())
    findAnswer(num1, num2)


def add(num1, num2):
    print("addition = ", (num1) + (num2))


def sub(num1, num2):
    print("substraction = ", (num1) - (num2))


def product(num1, num2):
    print("product = ", (num1) * (num2))


def qoutiant(num1, num2):
    print("qoutiant = ", (num1) / (num2))


def reminder(num1, num2):
    print("reminder = ", (num1) % (num2))


def findAnswer(a, b):
    add(a, b)
    sub(a, b)
    product(a, b)
    qoutiant(a, b)
    reminder(a, b)


main()
