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
