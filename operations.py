#Receive a list of arguments, add them and return the result.
def add(args):
    acc = 0
    for number in args:
        acc = acc + number
    return acc

#Receive a list of arguments, subtract them and return the result.
def subtract(args):
    acc = args[0]
    for i in range(1, len(args)):
        acc = acc - args[i]
    return acc

#Receive a list of arguments, multiply them and return the result.
def multiply(args):
    acc = 1
    for number in args:
        acc = acc * number
    return acc

#Receive a list of arguments, divide them and return the result.
def divide(args):
    acc = args[0]
    for i in range(1, len(args)):
        acc = acc / args[i]
    return acc


def printError():
    print("Enter with the following arguments:")
    print("-a, --add             add all the numbers passed as arguments")
    print("-s, --subtract        subtract all the numbers passed as arguments")
    print("-m, --multiply        multiply all the numbers passed as arguments")
    print("-d  --divide          divide all the numbers passed as arguments")