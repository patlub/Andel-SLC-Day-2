def data_type(arg):
    """
    Function to to test the data_type of
    argument passed to function
    Args:
         arg: Argument passed to function

    """
    if arg is None:
        return 'no value'

    # check for string type
    elif isinstance(arg, str):
        return len(arg)

    # check for Boolean type
    elif isinstance(arg, bool):
        return arg

    # check for integer type
    elif isinstance(arg, int):
        if arg == 100:
            return 'equal to 100'
        elif arg < 100:
            return 'less than 100'
        else:
            return 'more than 100'
