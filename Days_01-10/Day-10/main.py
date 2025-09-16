from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def Calculator():
    should_continue = True
    num1 = float(input("What is the first number?: "))
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")

        if operation_symbol not in operations:
            print("Invalid operation symbol. Please try again.")
            continue

        num2 = float(input("What is the next number?: "))
        result = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        continue_calc = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or 'e' to exit: ").lower()
        if continue_calc == 'y':
            num1 = result
        elif continue_calc == 'n':
            should_continue = False
            print("\n" * 20)
            # Start a new calculation if desired
            Calculator()
        else:
            print("goodbye")
            break


Calculator()
