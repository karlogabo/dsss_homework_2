import random

def round_if_not_integer(value):
    """
    Round if not integer.

    Args:
        value (int, float): value to be rounded

    Returns:
        int: rounded value

    """
    try:
        rounded_value = int(value)
    except ValueError:
        rounded_value = round(float(value))
        print(f"The value was not an integer. Rounded value: {rounded_value}")

    return rounded_value

def random_integer(min, max):
    """
    Random integer.

    Args:
        min (int): minimum value from which a random value with be taken
        max (int): maximum value from which a random value with be taken

    Returns:
        int: random value between minimum and maximum boundary

    """

    min = round_if_not_integer(min)
    max = round_if_not_integer(max)

    return random.randint(min, max)


def random_operator():
    """
    Random operator.

    Args:

    Returns:
        str: random operator

    """
    return random.choice(['+', '-', '*'])


def random_operation(a, b, operator):
    """
    Random operation.

    Args:
        a (int): value a
        b (int): value b
        operator (str): operator which will be used

    Returns:
        str: calculation statement
        int: performs calculation between "a" and "b" depending on "operator"

    """

    a = round_if_not_integer(a)
    b = round_if_not_integer(b)

    display = f"{a} {operator} {b}"
    if operator == '+': output = a + b
    elif operator == '-': output = a - b
    else: output = a * b
    return display, output

def math_quiz():
    points = 0
    i = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(i):
        n1 = random_integer(1, 10); n2 = random_integer(1, 5.5); o = random_operator()

        PROBLEM, ANSWER = random_operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            points += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {points}/{i}")

if __name__ == "__main__":
    math_quiz()
