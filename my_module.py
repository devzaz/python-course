print("Imported my module")

test = "Test String"

def find_index(to_search, target):
    """
    this will search for any elements inside a list and will
    return the index
    otherwie it will return -1
    """

    for i, value in enumerate(to_search):
        if value == target:
            return i


    return -1
