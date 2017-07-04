def fizz_buzz(number):
    """
    A function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz',
    or the argument it receives, all depending on the argument
    of the function, a number that is divisible by, 3, 5, or
    both 3 and 5, respectively

    Args:
        number:
    """
    if not isinstance(number, int) or number <= 0:
        return 'Invalid Argument'

    else:
        if (number % 3 == 0 and number % 5 == 0):
            return 'fizzBuzz'
        elif (number % 3 == 0):
            return 'fizz'
        elif (number % 5 == 0):
            return 'buzz'
        else:
            return number
